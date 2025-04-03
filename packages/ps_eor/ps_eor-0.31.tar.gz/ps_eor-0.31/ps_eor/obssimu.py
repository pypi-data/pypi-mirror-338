# Function and class to estimate experiments sensitivity
#
# Authors: F.Mertens


import os
import itertools

import numpy as np

import scipy.interpolate

import astropy.constants as const

from fast_histogram import histogram2d

INSTRU_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instru')


def enu_to_xyz_matrix(lat_rad):
    return np.array([
        [0, -np.sin(lat_rad), np.cos(lat_rad)],
        [1, 0, 0],
        [0, np.cos(lat_rad), np.sin(lat_rad)]
    ])


def xyz_to_uvw_matrix(ha_rad, dec_rad):
    return np.array([[np.sin(ha_rad), np.cos(ha_rad), 0.0],
                    [-np.sin(dec_rad) * np.cos(ha_rad), np.sin(dec_rad) * np.sin(ha_rad), np.cos(dec_rad)],
                    [np.cos(dec_rad) * np.cos(ha_rad), - np.cos(dec_rad) * np.sin(ha_rad), np.sin(dec_rad)]])



class Telescope(object):

    name = 'none'
    pb_name = name
    n_elements_per_stations = 1
    latitude = 0
    only_drift_mode = False
    redundant_array = False
    redundant_baselines = []
    stat_pos_is_enu = False
    umin = 0
    umax = 10000

    def get_stat_pos_file(self):
        pass

    def get_stat_pos(self):
        return np.loadtxt(self.get_stat_pos_file())

    def get_sefd(self, freq):
        pass

    def sky_temperature(self, freq, tsys_sky=60, temp_power_law_index=2.55):
        lamb = const.c.value / freq
        return tsys_sky * lamb ** temp_power_law_index

    def get_dipole_aeff(self, freq, distance_between_dipole):
        lamb = const.c.value / freq
        return np.min([lamb ** 2 / 3, np.ones_like(lamb) * np.pi * distance_between_dipole ** 2 / 4.], axis=0)

    def get_dish_aeff(self, freq, diameter, efficiency):
        lamb = const.c.value / freq
        return lamb ** 2 / (4 * np.pi) * efficiency * (np.pi * diameter / lamb) ** 2

    @staticmethod
    def from_name(name):
        if name.startswith('hera'):
            name.split('_')
        klasses = Telescope.__subclasses__()
        [klasses.extend(k.__subclasses__()) for k in klasses[:]]

        for klass in klasses:
            if hasattr(klass, 'name') and klass.name == name:
                return klass()

        raise ValueError('No telescope with name: %s' % name)


class DEx(Telescope):
    ''' Lunar interferometer, contributed by Sonia Ghosh '''
    name = 'dex'
    umin = 0.5
    umax = 25
    fov = 120
    du = 1
    only_drift_mode = True
    pb_name = name
    latitude = -26.70122102627586
    longitude = 116.67081524
    stat_pos_is_enu = True
    pb_name = 'ant_5_1.02_gaussian'

    def __init__(self, n_antenna_side=32, sep_antenna=6):
        Telescope.__init__(self)
        self.sep_antenna = sep_antenna
        self.n_antenna_side = n_antenna_side

    def get_stat_pos(self):
        grid_indices = np.arange(0, self.n_antenna_side)
        p_east, p_north = np.meshgrid(self.sep_antenna * grid_indices, self.sep_antenna * grid_indices)
        
        east = p_east.flatten()
        north = p_north.flatten()
        up = np.zeros_like(east)

        return np.vstack((east, north, up)).T

    def get_sefd(self, freq, tsys_sky=60):
        tsys = self.sky_temperature(freq, tsys_sky)
        a_eff = self.get_dipole_aeff(freq, self.sep_antenna)
        return 2 * const.k_B.value / a_eff * 1e26 * tsys


class SkaLow(Telescope):

    name = 'ska_low'
    umin = 30
    umax = 250
    fov = 3
    du = 8
    pb_name = name
    latitude = -26.703
    stat_pos_is_enu = True

    def get_stat_pos_file(self):
        # return os.path.join(INSTRU_DIR, 'ska1_low_sept2016_rot_statpos.data')
        return os.path.join(INSTRU_DIR, 'ska1_low_enu_statpos.data')

    def get_sefd(self, freq, tsys_sky=60):
        # Specification extracted from SKA LFAA Station design report document (https://arxiv.org/pdf/2003.12744v2.pdf).
        # See Page 22 of the report. SKALA v4 is actually expected to be better than the spec.
        freqs_spec = np.array([50, 80, 110, 140, 160, 220]) * 1e6
        a_eff_over_tsys_spec = 1 * np.array([0.14, 0.46, 1.04, 1.15, 1.2, 1.2])
        def t_sky_fct(freqs): return tsys_sky * (3e8 / freqs) ** 2.55
        a_eff_fct = scipy.interpolate.interp1d(freqs_spec, a_eff_over_tsys_spec * t_sky_fct(freqs_spec), 
                                               kind='slinear', bounds_error=False, fill_value='extrapolate')

        return 2 * const.k_B.value * 1e26 * t_sky_fct(freq) / a_eff_fct(freq)


class SkaLowAAstar(SkaLow):

    name = 'ska_low_aastar'
    stat_pos_is_enu = True

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'ska1_low_aastar_enu_statpos.data')


class LofarHBA(Telescope):

    name = 'lofar_hba'
    umin = 50
    umax = 250
    fov = 4
    du = 8
    n_elements_per_stations = 2
    pb_name = name
    latitude = 52.915

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'lofar_rot_statpos.data')

    def get_sefd(self, freq):
        # Typical observed SEFD ~ 130-160 MHz @ NCP (see https://old.astron.nl/radio-observatory/astronomers/lofar-imaging-capabilities-sensitivity/sensitivity-lofar-array/sensiti)
        return 4000


class A12HBA(Telescope):

    name = 'a12_hba'
    umin = 10
    umax = 200
    fov = 24
    du = 2
    pb_name = name
    n_elements_per_stations = 48
    latitude = 52.915

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'aartfaac_a12_hba_rot_statpos.data')

    def get_sefd(self, freq):
        # Typical observed SEFD of LOFAR-HBA between ~ 130-160 MHz @ NCP (see https://old.astron.nl/radio-observatory/astronomers/lofar-imaging-capabilities-sensitivity/sensitivity-lofar-array/sensiti)
        # LOFAR-HBA core is composed of 24 tiles. So S_tile = S_station * 24
        return 4000 * 24


class A12LBA(Telescope):

    name = 'a12_lba'
    umin = 20
    umax = 40
    fov = 120
    du = 1
    pb_name = 'ant_1.9_1.1_gaussian'
    n_elements_per_stations = 48
    latitude = 52.915
    only_drift_mode = True

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'aartfaac_a12_lba_rot_statpos.data')

    def get_sefd(self, freq, tsys_sky=60):
        distance_between_dipole = 7
        tsys = self.sky_temperature(freq, tsys_sky)
        a_eff = self.get_dipole_aeff(freq, distance_between_dipole)

        return 2 * const.k_B.value / a_eff * 1e26 * tsys


class MWA1(Telescope):

    name = 'mwa1'
    umin = 18
    umax = 80
    fov = 30
    du = 2
    pb_name = 'ant_4_1.05_gaussian'
    latitude = -26.70122102627586
    only_drift_mode = False

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'mwa_rev1_rot_statpos.data')

    def get_sefd(self, freq, tsys_sky=60):
        distance_between_dipole = 1.1
        n_dipole_per_stations = 4 * 4
        tsys = self.sky_temperature(freq, tsys_sky)
        a_eff = n_dipole_per_stations * self.get_dipole_aeff(freq, distance_between_dipole)

        return 2 * const.k_B.value / a_eff * 1e26 * tsys


class HERA(Telescope):
    name = 'hera'
    pb_name = 'ant_14_1.1_gaussian'
    latitude = -30.72146
    longitude = 21.42822
    only_drift_mode = True
    redundant_array = True
    redundant_baselines = np.array([14.6, 25.28794179, 29.2, 38.62796914, 43.8, 
                                    50.57588358, 52.64104862, 58.4, 63.63992458, 
                                    66.90560515, 73., 75.86382537, 77.25593828, 
                                    81.2893597, 87.6])
    umin = 4
    umax = 200
    du = 1
    stat_pos_is_enu = True

    def __init__(self, hex_num=11, split_core=True, sep=14.6):
        self.hex_num = hex_num
        self.split_core = split_core
        self.sep = sep

    def get_stat_pos(self):
        # Taken from https://github.com/HERA-Team/hera_sim/blob/main/hera_sim/antpos.py. Credit: HERA team.
        positions = []
        for row in range(self.hex_num - 1, -self.hex_num + self.split_core, -1):
            # adding self.split_core deletes a row if it's true
            for col in range(2 * self.hex_num - abs(row) - 1):
                x_pos = self.sep * ((2 - (2 * self.hex_num - abs(row))) / 2 + col)
                y_pos = row * self.sep * np.sqrt(3) / 2
                positions.append([x_pos, y_pos, 0])
                
        # basis vectors (normalized to self.sep)
        up_right = self.sep * np.asarray([0.5, np.sqrt(3) / 2, 0])
        up_left = self.sep * np.asarray([-0.5, np.sqrt(3) / 2, 0])

        # split the core if desired
        if self.split_core:
            new_pos = []
            for pos in positions:
                # find out which sector the antenna is in
                theta = np.arctan2(pos[1], pos[0])
                if pos[0] == 0 and pos[1] == 0:
                    new_pos.append(pos)
                elif -np.pi / 3 < theta < np.pi / 3:
                    new_pos.append(np.asarray(pos) + (up_right + up_left) / 3)
                elif np.pi / 3 <= theta < np.pi:
                    new_pos.append(np.asarray(pos) + up_left - (up_right + up_left) / 3)
                else:
                    new_pos.append(pos)
            # update the positions
            positions = new_pos

        return np.array(positions)

    def get_sefd(self, freq, tsys_sky=60):
        d = 14
        eff = 0.78
        trxc = 100

        lamb = const.c.value / freq
        a_eff = self.get_dish_aeff(freq, d, eff)
        tsys = tsys_sky * lamb ** 2.55 + trxc
        return 2 * const.k_B.value / a_eff * 1e26 * tsys


class HERA56(HERA):
    name = 'hera_56'

    def __init__(self):
        HERA.__init__(self, 5)


class HERA120(HERA):
    name = 'hera_120'

    def __init__(self):
        HERA.__init__(self, 7)


class HERA208(HERA):
    name = 'hera_208'

    def __init__(self):
        HERA.__init__(self, 9)


class HERA320(HERA):
    name = 'hera_320'

    def __init__(self):
        HERA.__init__(self, 11)


class NenuFAR(Telescope):

    name = 'nenufar'
    pb_name = 'nenufar'
    latitude = 47.37
    umin = 6
    umax = 60
    fov = 16
    du = 4
    latitude = 47.37

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'nenufar_full_rot_statpos.data')

    def inst_temperature(self, freq):
        """ Instrument temperature at a given frequency ``freq``.

            From: https://github.com/AlanLoh/nenupy/blob/master/nenupy/instru/instru.py
        """
        lna_sky = np.array([
            5.0965, 2.3284, 1.0268, 0.4399, 0.2113, 0.1190, 0.0822, 0.0686,
            0.0656, 0.0683, 0.0728, 0.0770, 0.0795, 0.0799, 0.0783, 0.0751,
            0.0710, 0.0667, 0.0629, 0.0610, 0.0614, 0.0630, 0.0651, 0.0672,
            0.0694, 0.0714, 0.0728, 0.0739, 0.0751, 0.0769, 0.0797, 0.0837,
            0.0889, 0.0952, 0.1027, 0.1114, 0.1212, 0.1318, 0.1434, 0.1562,
            0.1700, 0.1841, 0.1971, 0.2072, 0.2135, 0.2168, 0.2175, 0.2159,
            0.2121, 0.2070, 0.2022, 0.1985, 0.1974, 0.2001, 0.2063, 0.2148,
            0.2246, 0.2348, 0.2462, 0.2600, 0.2783, 0.3040, 0.3390, 0.3846,
            0.4425, 0.5167, 0.6183, 0.7689, 1.0086, 1.4042, 2.0732
        ])
        lna_freqs = (np.arange(71) + 15) * 1e6
        return self.sky_temperature(freq) * scipy.interpolate.interp1d(lna_freqs, lna_sky,
                                                                       bounds_error=False,
                                                                       fill_value='extrapolate')(freq)

    def get_sefd(self, freq, tsys_sky=60):
        distance_between_dipole = 5.5
        n_dipole_per_stations = 19
        tsys = self.sky_temperature(freq, tsys_sky) + self.inst_temperature(freq)
        a_eff = n_dipole_per_stations * self.get_dipole_aeff(freq, distance_between_dipole)

        return 2 * const.k_B.value / a_eff * 1e26 * tsys


class NenuFAR52(NenuFAR):

    name = 'nenufar_52'
    pb_name = 'nenufar'

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'nenufar52_rot_statpos.data')


class NenuFAR80(NenuFAR):

    name = 'nenufar_80'

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'nenufar80_rot_statpos.data')


class OVROLWA(Telescope):

    name = 'ovro_lwa'
    umin = 2
    umax = 60
    fov = 120
    du = 1
    pb_name = 'ant_1.9_1.1_gaussian'
    latitude = 37.23
    only_drift_mode = True
    stat_pos_is_enu = True

    def get_stat_pos_file(self):
        return os.path.join(INSTRU_DIR, 'ovro-lwa_statpos.data')

    def get_sefd(self, freq, tsys_sky=60):
        distance_between_dipole = 5
        tsys = self.sky_temperature(freq, tsys_sky)
        a_eff = self.get_dipole_aeff(freq, distance_between_dipole)

        return 2 * const.k_B.value / a_eff * 1e26 * tsys


class TelescopeSimu(object):

    def __init__(self, telescop: Telescope, freqs, dec_deg, hal, har, umin=None, umax=None, timeres=100, remove_intra_baselines=True):
        self.telescop = telescop
        self.freqs = freqs
        self.dec_deg = dec_deg
        self.hal = hal
        self.har = har
        self.umin = umin
        if self.umin is None:
            self.umin = telescop.umin
        self.umax = umax
        if self.umax is None:
            self.umax = telescop.umax
        self.timeres = timeres
        self.remove_intra_baselines = remove_intra_baselines

    @staticmethod
    def from_dict(d, freqs):
        def get_d_value(name, default=None):
            if default is None and not name in d:
                raise ValueError(f'{name} missing to initialize TelescopeSimu')
            return d.get(name, default)

        instru = get_d_value('PEINSTRU')
        dec_deg = get_d_value('PEOBSDEC')
        hal = get_d_value('PEOBSHAL')
        har = get_d_value('PEOBSHAR')
        timeres = get_d_value('PEOBSRES')
        remove_intra_baselines = get_d_value('PEREMINT')

        telescop = Telescope.from_name(instru)

        umin = get_d_value('PEOBSUMI', telescop.umin)
        umax = get_d_value('PEOBSUMA', telescop.umax)

        return TelescopeSimu(telescop, freqs, dec_deg, hal, har, umin=umin, umax=umax, 
                             timeres=timeres, remove_intra_baselines=remove_intra_baselines)

    def to_dict(self):
        return {'PEINSTRU': self.telescop.name, 'PEOBSDEC': self.dec_deg, 'PEOBSHAL': self.hal, 'PEOBSHAR': self.har,
                'PEOBSUMI': self.umin, 'PEOBSUMA': self.umax, 'PEOBSRES': self.timeres, 
                'PEREMINT': self.remove_intra_baselines}

    def simu_uv(self, include_conj=True):
        from ps_eor import psutil

        def m2a(m): return np.squeeze(np.asarray(m))

        lambs = const.c.value / self.freqs
        umin_meter = (self.umin * lambs).min()
        umax_meter = (self.umax * lambs).max()

        timev = np.arange(self.hal * 3600, self.har * 3600, self.timeres)

        statpos = self.telescop.get_stat_pos()
        nstat = statpos.shape[0]

        print('Simulating UV coverage ...')

        # All combinations of nant to generate baselines
        stncom = np.array(list(itertools.combinations(np.arange(0, nstat), 2)))
        print(f'Number of elements: {nstat}')
        print(f'Number of baselines: {stncom.shape[0]}')

        if self.remove_intra_baselines and self.telescop.n_elements_per_stations > 1:
            station_id = np.repeat(np.arange(0, nstat / self.telescop.n_elements_per_stations, dtype=int), self.telescop.n_elements_per_stations)
            stncom_stations = np.array(list(itertools.combinations(station_id, 2)))
            idx = np.array([a == b for a, b, in stncom_stations]).astype(bool)
            stncom = stncom[~idx]
            print(f'Discarding {idx.sum()} intra-baselines')

        b1, b2 = zip(*stncom)

        uu = []
        vv = []
        ww = []

        pr = psutil.progress_report(len(timev))
        i = 0

        for tt in timev:
            pr(i)
            ha_rad = (tt / 3600.) * (15. / 180) * np.pi
            dec_rad = self.dec_deg * (np.pi / 180)
            
            if self.telescop.stat_pos_is_enu:
                # from ENU to XYZ
                R = enu_to_xyz_matrix(np.radians(self.telescop.latitude))
                XYZ = np.dot(statpos, R)
            else:
                XYZ = statpos

            # from XYZ (rotated ECEF) to UVW
            R = xyz_to_uvw_matrix(ha_rad, dec_rad)
            statposuvw = np.dot(XYZ, R)

            bu = m2a(statposuvw[b1, 0] - statposuvw[b2, 0])
            bv = m2a(statposuvw[b1, 1] - statposuvw[b2, 1])
            bw = m2a(statposuvw[b1, 2] - statposuvw[b2, 2])

            ru = np.sqrt(bu ** 2 + bv ** 2)
            idx = (ru > umin_meter) & (ru < umax_meter)

            uu.extend(bu[idx])
            vv.extend(bv[idx])
            ww.extend(bw[idx])

            if include_conj:
                uu.extend(- bu[idx])
                vv.extend(- bv[idx])
                ww.extend(bw[idx])

            i += 1

        return np.array(uu), np.array(vv), np.array(ww)

    def redundant_gridding(self, max_distance=1):
        import sklearn.cluster
        from ps_eor import psutil, datacube

        uu_meter, vv_meter, _ = self.simu_uv()

        X = np.array([uu_meter, vv_meter]).T
        c = sklearn.cluster.DBSCAN(eps=max_distance, min_samples=1)
        c.fit(X)

        c_id, idx, counts = np.unique(c.labels_, return_index=True, return_counts=True)

        uu_meter_grid = uu_meter[idx]
        vv_meter_grid = vv_meter[idx]

        meta = datacube.ImageMetaData.from_res(0.01, (100, 100))
        meta.wcs.wcs.cdelt[2] = psutil.robust_freq_width(self.freqs)
        meta.set('PEINTTIM', self.timeres)
        meta.set('PETOTTIM', (self.har - self.hal) * 3600)

        w_cube = datacube.CartWeightsCubeMeter(np.repeat(counts[None, :], len(self.freqs), 0), 
                                               uu_meter_grid, vv_meter_grid, self.freqs, meta)

        return TelescopGridded(w_cube, self)

    def image_gridding(self, fov_deg, oversampling_factor=4, min_weight=10):
        from ps_eor import psutil, datacube

        uu_meter, vv_meter, _ = self.simu_uv()

        du = 1 / np.radians(fov_deg)
        res = 1 / (oversampling_factor * self.umax)
        n_u = int(np.ceil(1 / (res * du)))
        shape = (n_u, n_u)

        g_uu, g_vv = psutil.get_uv_grid(shape, res)

        ranges = [g_uu.min() - du / 2, g_uu.max() + du / 2]

        print('Gridding UV coverage ...')
        weights = []
        pr = psutil.progress_report(len(self.freqs))
        for i, lamb in enumerate(const.c.value / self.freqs):
            pr(i)
            w = histogram2d(uu_meter / lamb, vv_meter / lamb, bins=n_u, range=[ranges] * 2)
            weights.append(w)

        weights = np.array(weights)
        weights = weights.reshape(len(self.freqs), -1)
        g_uu = g_uu.flatten()
        g_vv = g_vv.flatten()
        ru = np.sqrt(g_uu ** 2 + g_vv ** 2)

        idx = (weights.min(axis=0) >= min_weight) & (ru >= self.umin) & (ru <= self.umax)
        weights = weights[:, idx]
        g_uu = g_uu[idx]
        g_vv = g_vv[idx]

        meta = datacube.ImageMetaData.from_res(res, shape)
        meta.wcs.wcs.cdelt[2] = psutil.robust_freq_width(self.freqs)
        meta.set('PEINTTIM', self.timeres)
        meta.set('PETOTTIM', (self.har - self.hal) * 3600)
        w_cube = datacube.CartWeightCube(weights, g_uu, g_vv, self.freqs, meta)

        return TelescopGridded(w_cube, self)


class TelescopGridded(object):

    def __init__(self, weights, telescope_simu):
        from ps_eor import psutil

        self.weights = weights
        self.telescope_simu = telescope_simu
        self.name = self.telescope_simu.telescop.name
        self.z = psutil.freq_to_z(self.weights.freqs.mean())

    def save(self, filename):
        self.weights.meta.update(self.telescope_simu.to_dict())
        self.weights.save(filename)

    @staticmethod
    def load(filename):
        from ps_eor import datacube

        weights = datacube.CartWeightCube.load(filename)
        telescope_simu = TelescopeSimu.from_dict(weights.meta.kargs, weights.freqs)

        if telescope_simu.telescop.redundant_array:
            weights = datacube.CartWeightsCubeMeter(weights.data, weights.uu, weights.vv, weights.freqs,
                                                    weights.meta, weights.uv_scale)

        return TelescopGridded(weights, telescope_simu)

    def get_tel_gridded_uv(self, freq_start=None, freq_end=None):
        from ps_eor import datacube

        if freq_start is None:
            freq_start = self.weights.freqs[0]
        if freq_end is None:
            freq_end = self.weights.freqs[-1]

        weights = self.weights.get_slice(freq_start, freq_end)

        if isinstance(weights, datacube.CartWeightsCubeMeter):
            m_freq = (freq_end + freq_start) / 2.
            weights = weights.get_cube(m_freq)

        return TelescopGriddedUV(weights, self.telescope_simu)


class TelescopGriddedUV(object):

    def __init__(self, weights, telescope_simu):
        from ps_eor import psutil

        self.weights = weights
        self.telescope_simu = telescope_simu
        self.name = self.telescope_simu.telescop.name
        self.z = psutil.freq_to_z(self.weights.freqs.mean())

    def get_slice(self, freq_start, freq_end):
        return TelescopGriddedUV(self.weights.get_slice(freq_start, freq_end), self.telescope_simu)

    def get_sefd(self):
        return np.atleast_1d(self.telescope_simu.telescop.get_sefd(self.weights.freqs))

    def get_ps_gen(self, filter_kpar_min=None, filter_wedge_theta=0):
        from ps_eor import pspec, datacube

        du = 0.75 / self.weights.meta.theta_fov

        if self.telescope_simu.telescop.redundant_array:
            mfreq = self.weights.freqs.mean()
            b = self.telescope_simu.telescop.redundant_baselines
            el = 2 * np.pi * b / (const.c.value / mfreq)
        else:
            el = 2 * np.pi * (np.arange(self.weights.ru.min(), self.weights.ru.max(), du))

        ps_conf = pspec.PowerSpectraConfig(el, window_fct='boxcar')
        ps_conf.filter_kpar_min = filter_kpar_min
        ps_conf.filter_wedge_theta = filter_wedge_theta
        ps_conf.du = self.telescope_simu.telescop.du
        ps_conf.umin = self.telescope_simu.umin
        ps_conf.umax = self.telescope_simu.umax
        ps_conf.weights_by_default = True

        eor_bin_list = pspec.EorBinList(self.weights.freqs)
        eor_bin_list.add_freq(1, self.weights.freqs.min() * 1e-6, self.weights.freqs.max() * 1e-6)
        eor = eor_bin_list.get(1, self.weights.freqs)
        pb = datacube.PrimaryBeam.from_name(self.telescope_simu.telescop.pb_name)

        return pspec.PowerSpectraCart(eor, ps_conf, pb)

    def get_noise_std_cube(self, total_time_sec, sefd=None, min_weight=1):
        if sefd is None:
            sefd = self.get_sefd()
        noise_std = self.weights.get_noise_std_cube(sefd, total_time_sec)
        noise_std.filter_min_weight(min_weight)

        return noise_std

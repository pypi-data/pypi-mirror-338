from unittest import TestCase

import pytest

import ldcpy

ds = ldcpy.open_datasets(
    'cam-fv',
    ['TS'],
    [
        'data/cam-fv/orig.TS.100days.nc',
        'data/cam-fv/zfp1.0.TS.100days.nc',
        'data/cam-fv/zfp1e-1.TS.100days.nc',
    ],
    ['orig', 'recon', 'recon2'],
)
ds2 = ldcpy.open_datasets(
    'cam-fv',
    ['PRECT'],
    [
        'data/cam-fv/orig.PRECT.60days.nc',
        'data/cam-fv/zfp1e-7.PRECT.60days.nc',
        'data/cam-fv/zfp1e-11.PRECT.60days.nc',
    ],
    ['orig', 'recon', 'recon2'],
)
ds3 = ldcpy.open_datasets('cam-fv', ['T'], ['data/cam-fv/cam-fv.T.3months.nc'], ['orig'])


class TestPlot(TestCase):
    """
    Note: The tests in this class currently only test the plot() function in ldcpy.plot for a variety of different
    parameters. Tests still need to be written for the methods in the plot.py class.
    """

    def test_magnitude_diff(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='magnitude_diff_ew',
            vert_plot=True,
            tex_format=False,
            weighted=False,
        )
        self.assertTrue(True)

    def test_real_information(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig'],
            calc='real_information',
            vert_plot=True,
            tex_format=False,
            weighted=False,
            plot_type='1D',
        )
        self.assertTrue(True)

    def test_real_information_cutoff(self):
        my_data = ds['TS'].sel(collection='orig').isel(time=0)
        my_data.attrs['data_type'] = ds.data_type
        my_data.attrs['set_name'] = 'orig'
        # Here just ask for the spatial mean at the first time step
        ds_calcs_across_space = ldcpy.Datasetcalcs(my_data, 'cam-fv', ['lat', 'lon'])
        # trigger computation
        d = ds_calcs_across_space.get_single_calc('real_information_cutoff')
        print(d)
        self.assertTrue(True)

    def test_fft2(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='fft2',
            vert_plot=True,
            tex_format=False,
            weighted=False,
        )
        self.assertTrue(True)

    def test_dataset_calc(self):
        my_data = ds['TS'].sel(collection='orig')
        my_data.attrs['cell_measures'] = 'area: cell_area'

        ds_calcs_across_time = ldcpy.Datasetcalcs(my_data, 'cam-fv', ['time'])
        ds_calcs_across_space = ldcpy.Datasetcalcs(my_data, 'cam-fv', ['lat', 'lon'])

        ds_calcs_across_time.get_calc('mean')
        ds_calcs_across_space.get_calc('mean')
        self.assertTrue(True)

    def test_grouped_standardized_mean_time_series(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='standardized_mean',
            legend_loc='lower left',
            calc_type='calc_of_diff',
            plot_type='time_series',
            group_by='time.dayofyear',
            tex_format=False,
            lat=90,
            lon=0,
            vert_plot=True,
            short_title=True,
        )

    def test_mean(self):
        ldcpy.plot(ds, 'TS', sets=['orig', 'recon'], calc='mean', vert_plot=True, tex_format=False)
        self.assertTrue(True)

    def test_mean_ts(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='std',
            plot_type='time_series',
            vert_plot=True,
            tex_format=False,
        )
        self.assertTrue(True)

    def test_standardized_mean(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='standardized_mean',
            plot_type='time_series',
            lat=90,
            lon=0,
            calc_type='diff',
            vert_plot=True,
            tex_format=False,
        )
        self.assertTrue(True)

    def test_prob_neg(self):
        ldcpy.plot(ds2, 'PRECT', sets=['orig', 'recon'], calc='prob_negative', tex_format=False)
        self.assertTrue(True)

    def test_mean_compare(self):
        ldcpy.plot(
            ds, 'TS', sets=['orig', 'recon'], calc='mean', plot_type='spatial', tex_format=False
        )
        self.assertTrue(True)

    def test_lag1(self):
        ldcpy.plot(
            ds, 'TS', sets=['orig', 'recon'], calc='lag1', plot_type='spatial', tex_format=False
        )
        self.assertTrue(True)

    def test_lag1_first_difference(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='lag1_first_difference',
            plot_type='spatial',
            tex_format=False,
        )
        self.assertTrue(True)

    def test_annual_harmonic(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='ann_harmonic_ratio',
            calc_type='calc_of_diff',
            tex_format=False,
        )
        self.assertTrue(True)

    def test_pooled_variance_ratio(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon', 'recon2'],
            scale='log',
            calc='pooled_var_ratio',
            calc_type='diff',
            tex_format=False,
        )

    def test_std_dev_compare(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='std',
            color='cmo.thermal',
            plot_type='spatial',
            tex_format=False,
        )
        self.assertTrue(True)

    def test_mean_diff(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='mean',
            calc_type='diff',
            transform='log',
            tex_format=False,
        )
        self.assertTrue(True)

    def test_prob_negative_log_compare(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='prob_negative',
            color='coolwarm',
            transform='log',
            plot_type='spatial',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_log_odds_positive_compare(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='odds_positive',
            calc_type='ratio',
            transform='log',
            color='cmo.thermal',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_odds_positive_grouped(self):
        # comparison between mean TS values in col_ds for "orig" and "zfpA1.0" datasets
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='odds_positive',
            plot_type='time_series',
            group_by='time.month',
            vert_plot=True,
        )
        self.assertTrue(True)

    def test_prob_neg_compare(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='prob_negative',
            color='binary',
            plot_type='spatial',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_first_differences(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='w_e_first_differences',
            color='binary',
            plot_type='spatial',
            tex_format=False,
            weighted=False,
        )
        self.assertTrue(True is True)

    def test_derivative(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='w_e_derivative',
            color='binary',
            plot_type='spatial',
            tex_format=False,
            weighted=False,
        )
        self.assertTrue(True is True)

    def test_mean_abs_diff_time_series(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon', 'recon2'],
            calc='mean_abs',
            calc_type='diff',
            plot_type='time_series',
            tex_format=False,
        )
        self.assertTrue(True is True)

    #    @pytest.mark.nonsequential
    def test_mean_diff_time_series_subset(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['recon', 'orig'],
            calc_type='diff',
            calc='mean',
            plot_type='time_series',
            subset='first50',
            lat=44.56,
            lon=-123.26,
            tex_format=False,
        )
        self.assertTrue(True)

    def test_subset_lat_lon_ratio_time_series(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='mean',
            calc_type='ratio',
            group_by=None,
            subset='first50',
            lat=44.76,
            lon=-93.75,
            plot_type='time_series',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_periodogram_grouped(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='mean',
            calc_type='raw',
            plot_type='periodogram',
            group_by='time.dayofyear',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_winter_histogram(self):
        ldcpy.plot(
            ds2,
            'PRECT',
            sets=['orig', 'recon'],
            calc='mean',
            calc_type='diff',
            subset='winter',
            plot_type='histogram',
            group_by='time.dayofyear',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_time_series_single_point_3d_data(self):
        ldcpy.plot(
            ds3,
            'T',
            sets=['orig'],
            calc='mean',
            plot_type='time_series',
            group_by='time.day',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_zscore_plot(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc_type='calc_of_diff',
            calc='zscore',
            tex_format=False,
        )
        self.assertTrue(True is True)

    def test_mae_max_day(self):
        ldcpy.plot(ds, 'TS', sets=['orig'], calc='mae_day_max', tex_format=False)

    def test_mean_3d(self):
        ldcpy.plot(ds3, 'T', sets=['orig'], calc='mean', lev=29, tex_format=False)
        self.assertTrue(True)

    def test_std_by_month(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='mean',
            plot_type='time_series',
            group_by='time.month',
            calc_type='diff',
            tex_format=False,
        )
        self.assertTrue(True)

    # Time series plot of first seven TS mean data points for ds orig dataset
    def test_mean_start_end(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig'],
            calc='mean',
            start=0,
            end=8,
            plot_type='time_series',
            tex_format=False,
        )
        self.assertTrue(True)

    def test_mean_time_series(self):
        ldcpy.plot(ds, 'TS', sets=['orig'], calc='mean', plot_type='time_series', tex_format=False)
        self.assertTrue(True)

    def test_periodogram(self):
        ldcpy.plot(ds, 'TS', sets=['orig'], calc='mean', plot_type='periodogram', tex_format=False)
        self.assertTrue(True)

    def test_plot_multiple_time_series(self):
        ldcpy.plot(
            ds,
            'TS',
            sets=['orig', 'recon'],
            calc='mean',
            plot_type='time_series',
            tex_format=False,
        )
        self.assertTrue(True)

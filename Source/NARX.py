from fireTS.core import GeneralAutoRegressor
from sklearn.utils.validation import check_X_y
from sklearn.metrics.regression import r2_score, mean_squared_error
import numpy as np

class DirectAutoRegressor(GeneralAutoRegressor):
    r"""
    This model performs autoregression with exogenous inputs on the k-step
    ahead output directly. The model equation is written as follows.

    .. math::
        y(t + k) &=& f(y(t), ..., y(t-p+1), \\
                & & x_1(t - d_1), ..., x_1(t-d_1-q_1+1), \\
                & & ..., x_m(t - d_1), ..., x_m(t - d_m - q_m + 1)) + e(t)
        :label: direct

    :param object base_estimator: an estimator object that implements the
                                  scikit-learn API (fit, and predict). The
                                  estimator will be used to fit the function
                                  :math:`f` in equation :eq:`direct`.
    :param int auto_order: the autoregression order :math:`p` in equation
                          :eq:`direct`.
    :param list exog_order: the exogenous input order, a list of integers
                            representing the order for each exogenous input,
                            i.e. :math:`[q_1, q_2, ..., q_m]` in equation
                            :eq:`direct`.
    :param int pred_step: the prediction step :math:`k` in equation :eq:`gar`.
                          By default, it is set to 1.
    :param list exog_delay: the delays of the exogenous inputs, a list of
                            integers representing the delay of each exogenous
                            input, i.e. :math:`[d_1, d_2, ..., d_m]` in
                            equation :eq:`direct`. By default, all the delays
                            are set to 0.
    :param dict base_params: other keyword arguments for base_estimator.
    """

    def __init__(self,
                base_estimator,
                auto_order,
                exog_order,
                pred_step,
                exog_delay=None,
                **base_params):
        super(DirectAutoRegressor, self).__init__(
            base_estimator,
            auto_order,
            exog_order,
            exog_delay=exog_delay,
            pred_step=pred_step,
            **base_params)

    def predict(self, X, y):
        r"""
        Produce multi-step prediction of y. The multi-step prediction is done
        directly. No future X inputs are used in the prediction. The prediction
        equation is as follows:

        .. math::
            \hat{y}(t + k) &=&  f(y(t), ..., y(t - p + 1), \\
                          & & x_1(t - d_1), ..., x_1(t - d_1 - q_1 + 1) \\
                          & & ..., x_m(t - d_m), ..., x_m(t - d_m - q_m + 1))

        :param array-like X: exogenous input time series, shape = (n_samples,
                            n_exog_inputs)
        :param array-like y: target time series to predict, shape = (n_samples)
        :param int step: prediction step.

        :return: k-step prediction time series, shape = (n_samples). The
                :math:`i` th value of the output is the k-step prediction of
                the :math:`i` th value of the input ``y``. The first
                ``pred_step + max(auto_order - 1, max(exog_order +
                exog_delay) - 1)`` values of the output is ``np.nan``.
        """
        # TODO: this allows nan in X and y, but might need more error checking
        X, y = np.array(X), np.array(y)
        if len(self.exog_order) != X.shape[1]:
            raise ValueError(
                'The number of columns of X must be the same as the length of exog_order.'
            )
        p = self._get_lag_feature_processor(X, y)
        features = p.generate_lag_features()
        yhat = self._predictNA(features)

        ypred = np.concatenate([np.empty(self.pred_step) * np.nan,
                                yhat])[0:len(y)]
        return ypred


    def score(self, X, y, method="r2", verbose=False):
        """
        Produce multi-step prediction of y, and compute the metrics against y.
        Nan is ignored when computing the metrics.

        :param array-like X: exogenous input time series, shape = (n_samples,
                            n_exog_inputs)
        :param array-like y: target time series to predict, shape = (n_samples)
        :param string method: could be "r2" (R Square) or "mse" (Mean Square
                              Error).

        :return: prediction metric. Nan is ignored when computing the metrics.
        """
        ypred = self.predict(X, y)
        mask = np.isnan(y) | np.isnan(ypred)
        if verbose:
            print('Evaluating {} score, {} of {} data points are evaluated.'.
                  format(method, np.sum(~mask), y.shape[0]))
        if method == "r2":
            return r2_score(y[~mask], ypred[~mask])
        elif method == "mse":
            return mean_squared_error(y[~mask], ypred[~mask])
# Version history:
from pandas.core.common import flatten

userID = 'YC_local'
printDebug = False

class descNames:
    def __init__(self):
        self.setNames()
        self.setBKvalues()
    def setNames(self):
        self.bk_short = ['b_inc', 'b_als', 'b_occ','b_purpose', 'b_property', 'b_tpo', 'b_state', 'b_servicer', 
            'b_cs', 'b_ltv', 'b_sato','b_dti', 'b_cpn', 'b_year', 'b_me', 'b_spread']

        self.bk_short_disc = ['b_occ','b_purpose', 'b_property', 'b_tpo', 'b_state', 'b_servicer', 'b_cpn', 'b_year', 'b_spread']

        self.info_cn = ['date', 'balance','count', 'wac', 'maturity', 'age', 'month', 'cpr', 'rht']
        self.tpo_cn = ['broker','corres','retail']
        self.occ_cn = ['invest', 'owner', 'second']
        self.property_cn = ['single', 'coop','condo', 'MH', 'PUD'] 
        self.purpose_cn = ['cashout', 'purchase', 'refi']
        self.state_cn = ['AZ', 'CA', 'CO', 'FL', 'GA', 'MD', 'MN', 'NV', 'NY', 'TX', 'VA', 'WA']
        self.servicer_cn = ['caliber', 'carrington', 'freedom', 'lakeview', 'loandepot', 'nationstar', 'newrez', 'pennymac', 'quicken', 'truist', 'usb', 'wfs']
        self.spread_cn = ['m21', 'adm15']

        self.servicer_code = [4213,3355,2094,4094,23725,3871,4150,4042,4052,4180,4206,4143]
        self.servicer_name = ['caliber','wfs','usb','pennymac','truist','freedom','lakeview','quicken','nationstar','loandepot','newrez','carrington']
        self.sprd_bucket = ['b_spread']
        self.sprd_feature = self.spread_cn

        self.disc_bucket_cn = ['b_tpo', 'b_occ', 'b_property', 'b_purpose', 'b_state', 'b_servicer']
        self.disc_feature = [ self.tpo_cn, self.occ_cn, self.property_cn, self.purpose_cn, self.state_cn, self.servicer_cn]

        self.cont_bucket_cn = ['b_inc', 'b_als', 'b_cs', 'b_ltv', 'b_sato', 'b_dti', 'b_me']
        self.cont_feature = ['incentive', 'als', 'cs',  'ltv', 'sato', 'dti', 'me']

        self.yc_cn = ['b_year', 'b_cpn']
        self.bucket_cn = self.cont_bucket_cn + self.disc_bucket_cn + self.sprd_bucket
        self.feature_cn = self.cont_feature + self.disc_feature + self.sprd_feature
        self.n_continuous = len(self.cont_bucket_cn)

        self.is_discrete = [False] * self.n_continuous + [True] * (len(self.bucket_cn)-self.n_continuous)
        self.up_slope = [1] * len(self.bucket_cn)
        for i in range(len(self.bucket_cn)):
            if 'ltv' in self.bucket_cn[i]:
                self.up_slope[i] = -1
            if 'sato' in self.bucket_cn[i]:
                self.up_slope[i] = -1
            if 'dti' in self.bucket_cn[i]:
                self.up_slope[i] = -1

        self.work_cn = ['b_cpn', 'b_year', self.bucket_cn, self.info_cn, self.feature_cn, 'rf']
        self.calib_cn = ['balance', self.feature_cn, 'rf']

        self.feature_cn_full = list(flatten(self.feature_cn))
        self.work_cn_full = list(flatten(self.work_cn))
        self.calib_cn_full = list(flatten(self.calib_cn))

    def setBKvalues(self):
        bucket_cn = self.bucket_cn
        cont_bucket_cn = self.cont_bucket_cn
        
        bk_values = []
        for c in bucket_cn:
            bv = []
            if c == 'b_state':
                bv = self.state_cn
            elif c == 'b_tpo':
                bv = self.tpo_cn
            elif c == 'b_occ':
                bv = self.occ_cn
            elif c == 'b_property':
                bv = self.property_cn
            elif c == 'b_purpose':
                bv = self.purpose_cn
            elif c == 'b_servicer':
                bv = self.servicer_cn
            elif c == 'b_ltv':
                bv = [50.0, 60.0, 70.0, 80.0, 100.0, 200]
            elif c == 'b_sato':
                bv = [-0.5, 0.0, 0.5, 1, 2, 5]
            elif c == 'b_cs':
                bv = [550, 650, 680, 720, 800, 1000]
            elif c == 'b_als':
                bv = [40000, 85000, 110000, 150000, 200000, 350000, 1000000]
            elif c == 'b_dti':
                bv = [0, 25, 30, 35, 40, 45, 100]
            elif c == 'b_me':
                bv = [0, 1]
            elif c == 'b_spread':
                bv = ['m21', 'adm15']
            elif c == 'b_inc':
                bv = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
            elif c != 'b_inc':
                print('Error name: ', c)
                sys.exit()
        
            if printDebug:
                print(c,'...', bv, len(bv))

            bk_values.append(bv)
                
        self.bk_values = bk_values
        
        
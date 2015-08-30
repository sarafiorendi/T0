"""
_InsertExpressConfigs_

Oracle implementation of InsertExpressConfigs

Insert Express configurations into Tier0 Data Service

"""

from WMCore.Database.DBFormatter import DBFormatter

class InsertExpressConfigs(DBFormatter):

    def execute(self, binds, conn = None, transaction = False):

        sql = """MERGE INTO express_config
                 USING DUAL ON ( run = :RUN AND stream = :STREAM )
                 WHEN MATCHED THEN
                   UPDATE SET cmssw = :CMSSW,
                              scram_arch = :SCRAM_ARCH,
                              reco_cmssw = :RECO_CMSSW,
                              reco_scram_arch = :RECO_SCRAM_ARCH,
                              alca_skim = :ALCA_SKIM,
                              dqm_seq = :DQM_SEQ,
                              global_tag = :GLOBAL_TAG,
                              scenario = :SCENARIO
                 WHEN NOT MATCHED THEN
                   INSERT (run, stream, cmssw, scram_arch, reco_cmssw, reco_scram_arch,
                           alca_skim, dqm_seq, global_tag, scenario)
                   VALUES (:RUN, :STREAM, :CMSSW, :SCRAM_ARCH, :RECO_CMSSW, :RECO_SCRAM_ARCH,
                           :ALCA_SKIM, :DQM_SEQ, :GLOBAL_TAG, :SCENARIO)
                 """

        self.dbi.processData(sql, binds, conn = conn,
                             transaction = transaction)

        return

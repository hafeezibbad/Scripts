#!/usr/bin/python
__author__ = 'eb'

import csv
import matplotlib.pyplot as plt
# packets for which no policy was available
no_policy_dict = {}
# packets for which policy was available
policy_available_dict = {}
# dictionary for storing records from analysis stats file
analysis_stats_dictionary = {}


class ControllerStatsData:
    """ This class stores the stats values obtained by the packet in controller class"""
    def __init__(self,id, decisionpacketTime, policyCheckingInterval,
                 policiesSearched, totalPolicies, policyHit, contAnalysisTime):
        self.packetId = id
        self.mkDecisionPacketTime = decisionpacketTime
        self.policyCheckInt = policyCheckingInterval
        self.polSearched = policiesSearched
        self.polTotal = totalPolicies
        self.polHit = policyHit
        self.contAnalysisTime = contAnalysisTime

    def display (self):
        return "Id: %d\n, DecisonPacketTime: %d\n, PolicyCheckInterval: %d\n, " \
               "PoliciesSearched: %d\n, TotalPolicies: %d\n, PolicyHit: %s\n " \
               "ControllerAnalysisTime: %d\n"


# get all values from controller stats file
def getControllerStats():
    contfile = open('/home/hafeez/times/controllerStats-noCM.csv', 'rb')
    contRead = csv.reader(contfile, delimiter=',')
    for row in contRead:
        if row[5] == 'true':
            # if policy is already available, then
            # total_time_to_make_decision = Time_to_make_decision_packet + time_to_check_relevant_policy
            policy_available_dict[row[0]] = ControllerStatsData(int(row[0]), float(row[1]), float(row[2]),
                                                                float(row[3]), float(row[4]), row[5], (float(row[1])+float(row[2])))
        else:
            no_policy_dict[row[0]] = ControllerStatsData(int(row[0]), float(row[1]), float(row[2]),
                                                                float(row[3]), float(row[4]), row[5], float(row[6]))

    print "All values %f read from controller stats file" % float(len(no_policy_dict)+len(policy_available_dict))

class AnalysisStatsData:
    """ This class stores the stats values obtained by the packet in analysis class"""
    def __init__(self, id, dockerParam, dockerAnalysis, totalAnalysis):
        self.packetId = id
        self.dockerParamTime = dockerParam
        self.dockerAnalysisTime = dockerAnalysis
        self.totalAnalysisTime = totalAnalysis

def getAnalysisStats():

    # get all values from analysis stats file
    analysisfile = open('/home/hafeez/times/analysisStats-noCM.csv', 'rb')
    analysisRead = csv.reader(analysisfile, delimiter=',')
    for row in analysisRead:
        analysis_stats_dictionary[row[0]] = AnalysisStatsData(int(row[0]), float(row[1]), float(row[2]), float(row[3]))

    print "All values %d read from analysis stats file" % len(analysis_stats_dictionary)


def doScience():
    analysisTime_sum = 0
    policyCheckInterval_sum = 0
    cont_no_pol_keys = no_policy_dict.keys()
    analysis_keys = analysis_stats_dictionary.keys()

    for key in cont_no_pol_keys:
        analysisTime_sum += no_policy_dict.get(key).contAnalysisTime
        policyCheckInterval_sum += no_policy_dict.get(key).policyCheckInt
    analysis_time_sum = 0
    for key in analysis_keys:
        analysis_time_sum += analysis_stats_dictionary.get(key).totalAnalysisTime

    print "Average analysis time = %f" % (analysisTime_sum / len(no_policy_dict))
    print "Average policy Checking time = %f" % (policyCheckInterval_sum / len(no_policy_dict))
    print "Average policy analysis time = %f" % (analysis_time_sum / len(analysis_stats_dictionary))

def policyCheckingLatency():
    keys = policy_available_dict.keys()
    policies_checked = []
    total_policies = []
    time_taken = []

    for key in keys:
        policies_checked.append(policy_available_dict.get(key).polSearched)
        total_policies.append(policy_available_dict.get(key).polTotal)
        time_taken.append(policy_available_dict.get(key).policyCheckInt)

    plt.plot(total_policies, time_taken, linestyle='--')
    plt.show()


def makePieChart():
    keys = no_policy_dict.keys()
    policy_check_avg = []
    policy_check_average = 0
    docker_param_acq_avg = []
    docker_param_time_average = 0
    docker_decision_time_avg = []
    docker_decision_time_average = 0
    interProcessTime_avg = []
    interProcessTime_average =0.0
    # times
    avg_processing_time = 0.0
    avg_analysis_processing_time = 0.0
    avg_internal_policy_check_time = 0.0
    avg_docker_analysis_time = 0.0
    avg_cm_comm_time = 0.0


    for key in keys:
        policy_check_avg.append(((no_policy_dict.get(key).policyCheckInt+no_policy_dict.get(key).mkDecisionPacketTime)/no_policy_dict.get(key).contAnalysisTime)*100)
        docker_param_acq_avg.append((analysis_stats_dictionary.get(key).dockerParamTime/no_policy_dict.get(key).contAnalysisTime)*100)
        docker_decision_time_avg.append((analysis_stats_dictionary.get(key).dockerAnalysisTime/no_policy_dict.get(key).contAnalysisTime)*100)

        interProcessTime_avg.append(((no_policy_dict.get(key).contAnalysisTime -
                                     (no_policy_dict.get(key).policyCheckInt+no_policy_dict.get(key).mkDecisionPacketTime + analysis_stats_dictionary.get(key).dockerParamTime +analysis_stats_dictionary.get(key).dockerAnalysisTime))
                                    /no_policy_dict.get(key).contAnalysisTime)*100)

    avg_processing_time += no_policy_dict.get(key).contAnalysisTime
    avg_analysis_processing_time += analysis_stats_dictionary.get(key).totalAnalysisTime
    avg_cm_comm_time += analysis_stats_dictionary.get(key).dockerParamTime
    avg_internal_policy_check_time += no_policy_dict.get(key).policyCheckInt
    avg_docker_analysis_time += analysis_stats_dictionary.get(key).dockerAnalysisTime

    print "Average total analysis time (from controller) %f nano seconds " % (avg_processing_time/len(no_policy_dict))
    print "Average total analysis time (from analysis) %f nano seconds " % (avg_analysis_processing_time/len(no_policy_dict))
    print "Average communication time with cloud manager (from analysis) %f nano seconds " % (avg_cm_comm_time/len(no_policy_dict))
    print "Average time for internal DB checking (from analysis) %f nano seconds " % (avg_internal_policy_check_time/len(no_policy_dict))
    print "Average time taken by docker to analyse (from analysis) %f nano seconds " % (avg_docker_analysis_time/len(no_policy_dict))

    # get averages of all values
    for i in range(len(policy_check_avg)):
        policy_check_average += policy_check_avg[i]
        docker_decision_time_average += docker_decision_time_avg[i]
        docker_param_time_average += docker_param_acq_avg[i]
        interProcessTime_average += interProcessTime_avg[i]

    print "Average policy checking time %f " % (policy_check_average/len(policy_check_avg))
    print "Average docker parameter acquisition time %f " % (docker_param_time_average/len(policy_check_avg))
    print "Average docker analysis time %f " % (docker_decision_time_average/len(policy_check_avg))
    print "Average Inter communication time %f " % (interProcessTime_average/len(policy_check_avg))

    plt.pie([(policy_check_average/len(policy_check_avg)),
             (docker_param_time_average/len(policy_check_avg)),
             (docker_decision_time_average/len(policy_check_avg)),
             (interProcessTime_average/len(policy_check_avg))])
    plt.axis('equal')
    plt.xticks(())
    plt.yticks(())
    axes = plt.gca()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    getControllerStats()
    getAnalysisStats()
    makePieChart()

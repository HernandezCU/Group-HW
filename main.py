# The Solar Project - (Because its not warm enough outside to be speaking about solar power)
#  You will submit this project individually but work collaboratively. You will also be graded as a team meaning
#  if 1 member does not submit the code to their repository, and response on blackboard
#  but the other 3 team members do both parts perfectly. The final grade project will be a 75% for everyone.
#
#  Black Board Submission
#    Submit a review of each member of the as part of the blackboard submission.
#    1. I am not expecting much here, just 2 or 3 sentences reviewing each team member.
#    2. What did you enjoy about the project?
#    3. What did you not enjoy?

#  Code Submission:
#    Use the data set for creating  /data/756874_system_power_20210207.csv
#    Required functions in the git repository are below and should be located under /homework/hw3.py
import csv
from datetime import datetime
from typing import Dict

file_CSV = open("756874_system_power_20210207.csv")
data_CSV = csv.reader(file_CSV)
list_CSV = list(data_CSV)


date_time, power = map(list, zip(*list_CSV))



def hourly_demand_summary() -> Dict[datetime, float]:
  
    hourly_dict = {}
    for x in range(0,len(date_time),12):
      start_ts = (datetime.strptime(date_time[x][0:19],"%Y-%m-%d %H:%M:%S"))
      temp_power = 0
      for i in range(x,x+12):
        temp_power =+ int(power[i])
        end_ts = (datetime.strptime(date_time[i][0:19],"%Y-%m-%d %H:%M:%S"))
      start_hour, year, ddate, month =  start_ts.strftime("%H"),start_ts.strftime("%Y"), start_ts.strftime("%d"), start_ts.strftime("%m")
      end_hour = end_ts.strftime("%H")
      hourly_dict[int(year),int(month),int(ddate),int(start_hour),int(end_hour)]=temp_power

    print(hourly_dict)
    return(hourly_dict)


def daily_demand_summary() -> Dict[datetime, float]:
    with open("756874_system_power_20210207.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dail_totals = {}
        line_count = 0
        string_day = "No day yet"
        previous_day = 0
        daily_total = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # print("Date: ", row[0], "Power: ", row[1])
                date = str(row[0])
                present_day = int(date[9])
                if present_day == previous_day:
                    daily_total += int(row[1])
                else:
                    dail_totals.update({string_day: daily_total})
                    previous_day = present_day
                    string_day = row[0]
                    daily_total = 0
    dail_totals.pop('No day yet', 0)
    return dail_totals
#HELLO MR CHERRY I am having trouble correctly formating the datetime of this dict, everything else works Ln 69 haha nice

def weekly_power_summary() -> float:
    c_to_int = [int(i) for i in power]
    summary = sum(c_to_int)

    return float(summary)


def maximum_hourly_data() -> datetime:
    date_time, power = map(list, zip(*list_CSV))
    res = [int(i) for i in power]
    largest = max(res)
    lday = res.index(largest)

    date_s = date_time[lday]
    rev_format = date_s.replace(' -0600', '')

    return rev_format


if __name__ == "__main__":
    print(daily_demand_summary())
    # weekly_power_summary()
    # print(daily_demand_summary())
    # print(maximum_hourly_data())
    # hourly_demand_summary()


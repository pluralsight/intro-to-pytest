from testrail_api import TestRailAPI

# from tests.helpers.jira_adaptor import JiraAdaptor
from time import sleep
from datetime import datetime


class TestRailUtils:
    def __init__(self):
        self.api = TestRailAPI('https://getupside.testrail.io/', 'testgetupside@gmail.com', 'M+r5`55{S8Ks')

    def create_a_new_run(self, name, test_cases):
        test_rail_run = {}
        now = datetime.now()
        dt_string = now.strftime(" - %d/%m/%Y %H:%M:%S")
        run = self.api.runs.add_run(name=name + dt_string, project_id=1,
                                    include_all=False,
                                    suite_id=369,
                                    case_ids=test_cases,
                                    assignedto_id=3)
        test_rail_run["name"] = name
        test_rail_run["id"] = run['id']
        return test_rail_run

    def close_run(self, run):
        self.api.runs.close_run(run)

    def get_current_run(self, test, created_runs):
        current_run = test['metadata']['testrail_run_name']
        return [run['id'] for run in created_runs if run['name'] == current_run][0]

    def get_test_result(self, test):
        test_result = test['outcome']
        result_dict = {'passed': 1, 'failed': 5, 'error': 5, 'skipped': 6}
        return result_dict[test_result]

    def get_test_name(self, test):
        test_name = test['metadata']['test_name']
        return test_name

    def get_test_case(self, test):
        test_case = test['metadata']['extra_kwargs']['tc']
        return test_case

    def get_screenshot(self, test):
        screenshot_url = test['metadata'].get('screen')
        return "![Screenshot] ({})".format(screenshot_url)

    def get_video(self, test):
        sleep(5)
        video_url = test['metadata'].get('automation_session').get('video_url')
        return "See the replay on [BrowserStack]({})".format(video_url)

    def get_logs(self, test):
        device_logs = test['metadata'].get('automation_session').get('device_logs_url')
        appium_logs = test['metadata'].get('automation_session').get('appium_logs_url')
        return "[Device logs]({}) \n [Appium logs]({})".format(device_logs, appium_logs)

    def get_session_id(self, test):
        session_id = test['metadata'].get('session_id')
        return session_id

    def get_app_version(self, test):
        version = test['metadata'].get('automation_session').get('app_details').get('app_version')
        return version

    def get_device(self, test):
        device = test['metadata'].get('device_name')
        os_version = self.get_os_version(test)
        return "{}, OS version {}".format(device, os_version)

    def get_platform(self, test):
        platform = test['metadata'].get('platform_name')
        return platform

    def get_os_version(self, test):
        os_version = test['metadata'].get('os_version')
        return os_version

    def get_error(self, test):
        if self.get_test_result(test) == 5:
            message = test['call'].get('crash').get('message')
            path = test['call'].get('crash').get('path')
            line = test['call'].get('crash').get('lineno')
            return """
                {}
                On file: {},
                line number: {}
                """.format(message, path, line)
        else:
            return None

    def add_test_result(self, test, created_runs, is_jira):
        run = self.get_current_run(test, created_runs)
        test_case = self.get_test_case(test)
        result = self.get_test_result(test)
        screenshot = self.get_screenshot(test) if result not in (6, ) else None
        video = self.get_video(test) if result not in (6, 2) else None
        logs = self.get_logs(test) if result not in (6, ) else None
        session_id = self.get_session_id(test) if result not in (6, ) else None
        version = self.get_app_version(test) if result not in (6, 2) else None
        device = self.get_device(test) if result not in (6, 2) else None
        platform = self.get_platform(test) if result not in (6, 2) else None
        test_name = self.get_test_name(test) if result not in (6, ) else None
        error = self.get_error(test)
        if (result == 5 or result == 2) and is_jira:
            jira_adaptor = JiraAdaptor()
            jira_adaptor.create_a_new_ticket(test_name=test_name, message=error,
                                             version=version, platform=platform,
                                             device=device, video=video,
                                             screenshot=screenshot, logs=logs
                                             )

        self.api.results.add_result_for_case(run_id=run, case_id=test_case,
                                             custom_build=version,
                                             custom_device=device, custom_video=video,
                                             custom_logs=logs, status_id=result,
                                             custom_screenshot=screenshot,
                                             custom_error=error, custom_session_id=session_id
                                             )

    def get_test_run_url(self, run_id):
        test_run = self.api.runs.get_run(run_id)
        return test_run['name'], test_run['url']


# r = ReportManager()
# t = TestRailUtils()
# runs = r.get_test_runs()
# cases = r.get_test_cases()
# tests = r.get_all_tests()
# #
# print(runs)
# print(cases)
# print(tests)
#
# created_runs = [t.create_a_new_run(run, cases) for run in runs]
# for test in tests:
#     t.add_test_result(test, created_runs)

# ids = t.api.cases.get_cases(project_id=1, suite_id=25)
# print(ids)

#
# t_runs = t.api.runs.get_runs(1)
# #
# print(t_runs)
#
# for run in t_runs:
#     print(t.api.runs.close_run(run['id']))



# t = TestRailUtils()
# print(t.api.reports.run_report(14))


import sys

def run_report(report_type='automation'):
    global report
    if report_type == 'automation':
        report = 13
    t = TestRailUtils()
    return t.api.reports.run_report(report)

if __name__ == "__main__":
    report = sys.argv[1]
    print(run_report(report)['report_url'])

from class_checker import Class_Checker_Bot
from connectcarolina_bot import RegistryBot
import cgi
'''
#cgi stuff
args = cgi.FieldStorage()
onyen = args['onyen']
password = args['password']
dept = args['department']
course_number = args['course_number']
class_number = args['class_number']

Class_Checker_Bot(onyen, password, dept, course_number, class_number)
'''

userid = raw_input("Onyen: ")
pw = raw_input("Password: ")

robot = RegistryBot(userid, pw)
robot.login()

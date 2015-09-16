from class_checker import Class_Checker_Bot
from connectcarolina_bot import RegistryBot
import cgi
pw = 'joking55!!!'
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


robot = RegistryBot('jmkay', pw)
robot.login()
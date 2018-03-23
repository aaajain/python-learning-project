
prerequisite:-
1. Python above 3.0 version.
2. pip version 9.0.3

steps after project checkout:-

1. Checkout project 
2. Go in the project directory i.e python project\StudentReportCard
3. Open cmd in above directory and type following command:-
                pip install -r requirement.txt
               
 
steps to follow when new dependencies added by individual

1. Go in project directory i.e  python project\StudentReportCard
2. Open cmd and type following command:-
                pip freeze > requirements.txt
3. It will create requirement.txt file with your latest added dependencies
4. Then checkin(push) requirement.txt file

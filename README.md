# What is this?
Templates and Test Suites for Programming Contests and Online interviews.

## Requirements
* Python 3.5 +

## How to Use
##### 1.Write a Main logic
* Write main logic at the main function of `src/bin/main.py`
  * This corresponds to the submission code for the contest.
  
##### 2.Write a Test
* Write either test case at `src/test/test_main.py` based on the type of submission.
  * If the contest site uses stdin/stdout for evaluation, Use `StdInOutTestCase`.
  * If the contest site uses return value for evaluation, Use `MainRoutineTestCase`.
  
##### 3.Execute the Test
* Then, execute unit test on project root by the following command.
    * `python -m unittest src.test.test_main.StdInOutTestCase` or
    * `python -m unittest src.test.test_main.MainRoutineTestCase`
    
## How to Contribute
* Please feel free to send pull-request to make the template more practical.

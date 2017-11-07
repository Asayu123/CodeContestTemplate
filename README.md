# CodeContestTemplate
an Template for Code Contest.

## Requirements
* Python 3.5 +

## How to Use
##### 1.Write a Main logic
* Comment out lines in helper method `_input_args` and `_output_result` at `src/bin/main.py` based on a problem.
* Write main logic at `src/bin/main.py`
##### 2.Write a Test
* Write test parameters on method `generate_subtest_case` at `src/test/test_main.py`
* Write test code of main logic on method `test_main` at `src/test/test_main.py`

##### 3.Execute the Test
* Then, execute unit test on project root by the following command.
    * `python -m unittest src/test/test_main.py`
    
* Now, You got a code for a contest.

## Tips
* Use git stash / unstash when you solve multiple problems at the same time.

## How to Contribute
* Please feel free to send pull-request to make the template more practical.

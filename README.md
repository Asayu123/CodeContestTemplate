# CodeContestTemplate
an Template for Code Contest.

## Requirements
* Python 3.5 +

## How to Use
##### 1.Write a Main logic
* Comment out lines in helper method `_input_args` and `_output_result` at `src/bin/main.py` based on a problem.
* Write main logic at `src/bin/main.py`
##### 2.Write a Test
* Make a test case that are the subclass of unittest.TestCase, with a custom Mixin 'EndToEndTestMixin'
  * Copying test/test_main.py and rename it is the quickest way to achieve this.
* Write test parameters as a class attribute of the TestCase.
* Append some additional test in that TestCase if you need.

##### 3.Execute the Test
* Then, execute unit test on project root by the following command.
    * `python -m unittest src/test/test_xxx.py`


## Tips
* Use git stash / unstash when you solve multiple problems at the same time.

## How to Contribute
* Please feel free to send pull-request to make the template more practical.

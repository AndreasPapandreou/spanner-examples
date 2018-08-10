# Spanner CI Test Examples #

## Introduction

This documentation's goal is to define a set of custom test scripts, to be used by the Spanner CI team as a guideline of what the libraries should look like, what kind of APIs we'd want to provide to our users, and finally how they woud be used in a script.

The secondary goal of these examples is to provide a future documentation to our users, which will help them use our product.

## Test Categories

The test cases are split into three categories:

1. **Basic Tests**, which only perform one action and one test, to showcase that individual test function
2. **Simple Tests**, which perform a simple real-world scenario, i.e. *Turn Light on through Network Command*
3. **Complex Tests**, which perform a more common and complex real-world scenario, and whose goal is to showcase what an actual Functional test for a real product would test, with more than one assertions and using multiple APIs.

Each of these have subcategories, such as GPIO, Networking, etc.

# Spanner CI - Quick Start Guide #

This is a quick start guide of Spanner CI.

## Register & Sign-In

##### To get started with Spanner CI, make sure to follow the steps below:

1. Visit http://console.spannerci.com
2. Click on register (or click on "sign in with github" button)*
3. Fill in the form with the appropriate information and click on the Register button.
4. Use the credentials provided above to sign-in to the SpannerCI platform.

\* By signing in with GitHub, the GitHub authorisation section below can be skipped.

## Integration with GitHub

Spanner provides an official Github Spanner CI Application for easy integration with GitHub. This authorises the Spanner CI platform to access the Github repositories. Please note that the account where the GitHub Spanner CI app is installed, must be the same as the one authorised using the GitHub sign in. 

####Installation of GitHub Spanner CI App:
1. Visit https://github.com/apps/spannerci-app
2. Click on install.
3. Select the repositories that you wish to provide access to the Spanner CI platform.


####GitHub Authorization:
1. After sign in the Spanner CI platform, click the username on the left upper corner.
2. Select Settings on the dropdown menu.
3. Click on the "Connect with Github" button to link the GitHub account with Spanner CI.
4. Spanner CI account is ready and authorised to use the selected GitHub repositories.

## Spanner Configuration

Add a .spannerci.json configuration file to your repository to enable Spanner integration. An example file is shown below:

    {
      "code_quality": false,
      "build_binary": false,
      "deploy": false,
      "script": "path/to/script/myscript.py"
    }
    
The most important setting of this file is the path of the Test script that contains your functional tests for your product. 

Example test scripts for various use cases can be found in our GitHub page: 
https://github.com/spannerci.

## Spanner Projects
Spanner supports the creation of one or more projects for working with different repos etc. To create a new project:

1. Select Projects from the navigation menu on the left side of the dashboard.
2. Click on New Project.
3. From there, a user can either add a new project manually or select a repository from the connected repositories on Github.
4. Click on create project.

## Spanner Jobs
Spanner executes each test script inside a virtual environment. For each run, a new job is created. Jobs can run automatically (through pull requests) or manually as described below.

### Manual Job Creation:
1. Click on projects, from the navigation menu on the left side of the dashboard.
2. Select the run by Branch or Commit option. By selecting run by commit, the commit id (sha hash) should manually be provided. By selecting the branch option, an available branch from the repository can be selected.
3. Click on the Play Button to start the new job.
4. If any errors have occurred, an alert message will appear prompting the error on the test script.
5. If the test has completed successfully, a message will appear and the user will be redirected to the Jobs page.

### Job Creation from Pull Request

This will automatically trigger a Spanner CI Job on each Pull Request ***

1. Click on the Pull request button in the Github Repository homepage.
2. Create a new Pull request and wait for the notification messages delivered from the SpannerCI platform.
3. After the completion of the test cases, a message will appear together with a link to the SpannerCI platform with more information, on the run itself.


### Job History

1. Click on Jobs from the navigation menu on the left side of the dashboard.
2. A list of the latest running jobs will be shown.
3. By clicking the Stats button on each job, enables us to watch each running test and their corresponding results.

## Spanner CLI
Spanner provides a Command Line Interface (CLI) which can be used instead of the Web Interface. For more information please contact us.

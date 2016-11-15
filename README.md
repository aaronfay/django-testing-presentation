# django-testing-presentation

This is a quick presentation showing a few different ways in which we can
test a Django application. It is by no means a comprehensive look at testing
(as if you could do such a thing) but is more intended to serve 2 purposes:

 * show you some examples of how to get started
 * convince you that you should *just get testing*, whatever that looks like

## the test case
The scenario under test is simple:

    > when a user submits their email in the form
    < then the email is saved

You can find 3 different testing examples in the different branches of this
repo:

 * branch `a` (this branch) has The Django Way™ of testing, using
   `django.test.TestCase` and `django.test.Client`
 * branch `b` uses `unittest.TestCase`, `unittest.mock.Mock` and
   `unittest.mock.patch` to test the same view
 * branch `c` pulls the business logic out of the view (ala Uncle Bob) and
   uses `unittest.mock.patch` to mock out the database layer


## the code

The areas of interest in this repo will primarily be `hackers.views` and
`hackers.tests`. If you toggle branches viewing those files you will see
the primary differences in the test approaches.

## the slides

You can find the slides for my talk by [clicking here][1].

[1]: https://docs.google.com/presentation/d/19ILWpChMwt6fqWfg4VLXoFTd5pR12ah_uXXvAy1ylXg/edit?usp=sharing
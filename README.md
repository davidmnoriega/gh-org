# gh-org
GitHub Organization Management

[![Build Status](https://travis-ci.org/davidmnoriega/gh_org.svg?branch=develop)](https://travis-ci.org/davidmnoriega/gh_org)
[![Coverage Status](https://coveralls.io/repos/github/davidmnoriega/gh_org/badge.svg?branch=develop)](https://coveralls.io/github/davidmnoriega/gh_org?branch=develop)

The aim of this project is to make managing a large GitHub organization easier by using LDAP and
Terraform.

User information will be stored in LDAP and used to generate a Terraform file that can be used by
their GitHub provider to manage which users are in the organization. This application will also
utilize personal access tokens to read a user's email list and verify that the email in LDAP is
listed in a user's profile. Should a user's information retrieved from GitHub not match LDAP, they
will not be added to the org's user list. When a user is no longer found in LDAP, they will be
removed from the user list and removed from the org at the next `terraform apply`.

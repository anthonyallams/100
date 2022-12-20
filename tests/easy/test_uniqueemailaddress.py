import pytest
from easy.uniqueemailaddress import numUniqueEmails,numUniqueEmails1


def test_uniqueemailaddress():
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    assert numUniqueEmails(emails) == 2
    assert numUniqueEmails(emails2) == 3
    assert numUniqueEmails1(emails) == 2
    assert numUniqueEmails1(emails2) == 3
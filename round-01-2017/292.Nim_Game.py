#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            return True
        else:
            return bool(n % 4)

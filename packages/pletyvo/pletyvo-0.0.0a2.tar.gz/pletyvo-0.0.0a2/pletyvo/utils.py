# Copyright (c) 2025 Osyah
# SPDX-License-Identifier: MIT


def padd(s: str) -> str:
    return s + "=" * (-len(s) % 4)

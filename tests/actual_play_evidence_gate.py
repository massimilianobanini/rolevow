"""Validate provenance for independent English actual-play evidence records.

Does not inspect a model's behavior or judge game quality. Blank/synthetic data
can never count as independent actual play PASS.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

CASE_IDS = tuple(f'T{i:02d}' for i in range(1,21))


def count_verified_actual_play(records: list[dict[str, Any]]) -> tuple[int, list[str]]:
    seen=set(); verified=0; errors=[]
    for item in records:
        case=item.get('id')
        if case not in CASE_IDS or case in seen:
            errors.append(f'Invalid or duplicate case id: {case}')
            continue
        seen.add(case)
        status=item.get('status', 'NOT_RUN')
        if status not in ('NOT_RUN','PASS','FAIL','BLOCKED'):
            errors.append(f'Invalid status for {case}')
            continue
        if status != 'PASS':
            continue
        required=('mode','candidate_sha256','source_files','user_input','assistant_output',
                  'reviewer','reviewer_verdict','privacy_reviewed')
        missing=[k for k in required if not item.get(k)]
        if missing:
            errors.append(f'{case} PASS lacks evidence: '+','.join(missing))
            continue
        if item.get('mode') != 'independent_fresh_chat':
            errors.append(f'{case} is not independent fresh-chat evidence')
            continue
        if item.get('reviewer_verdict') != 'PASS' or item.get('privacy_reviewed') is not True:
            errors.append(f'{case} reviewer/privacy gate not cleared')
            continue
        if case == 'T20' and (item.get('human_participants', 0)<2 or item.get('participant_consent') is not True):
            errors.append('T20 requires >=2 human participants and explicit evidence consent')
            continue
        verified += 1
    for case in CASE_IDS:
        if case not in seen:
            errors.append(f'Missing case record: {case}')
    return verified,errors

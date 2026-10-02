#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanceur autonome pour la suite de tests E2E L'OCHJU.
Usage:
    python tests/e2e/run_tests.py
"""

import sys
from pathlib import Path

# Ajouter le dossier courant au path pour importation directe
current_dir = Path(__file__).parent.resolve()
sys.path.insert(0, str(current_dir))

from test_suite_e2e_lochju import LochjuE2ETestRunner

if __name__ == "__main__":
    runner = LochjuE2ETestRunner()
    report = runner.run_all()
    failed = report["summary"]["failed"]
    print(f"\n[Test Runner] Fin d'exécution — {report['summary']['passed']}/{report['summary']['total_assertions']} tests passés.")
    sys.exit(0 if failed == 0 else 1)

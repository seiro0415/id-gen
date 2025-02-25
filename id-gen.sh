#!/bin/bash

# 스크립트의 실제 위치를 찾아서 프로젝트 루트 경로 설정
SCRIPT_PATH=$(readlink -f "$0")
PROJECT_ROOT=$(dirname "$SCRIPT_PATH")

# 가상환경의 Python 실행
"$PROJECT_ROOT/.env/bin/python" "$PROJECT_ROOT" "$@"

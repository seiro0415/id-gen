# id-gen - A simple ID generator

간단한 식별자를 생성하는 커맨드라인 도구다. 생성되는 식별자는 다음 규칙을 따른다:

- 소문자 알파벳으로 시작
- 소문자 알파벳과 숫자의 조합
- 최소 1개의 숫자 포함

## Installation

Python 환경 설정:

```bash
pyenv shell 3.13
python -m venv .env
source .env/bin/activate
```

프로젝트 실행:

```bash
python .
```

## Usage

```bash
# 기본 실행 (랜덤 길이로 1개 생성)
python .

# 짧은 길이(5자리) 식별자 생성
python . -s

# 중간 길이(7자리) 식별자 생성
python . -m

# 긴 길이(11자리) 식별자 생성
python . -l

# 여러 개의 식별자 생성 (예: 3개)
python . -n 3

# 특정 길이로 여러 개 생성
python . -s -n 3  # 5자리 식별자 3개
```

## 식별자 길이

- 짧은 길이 (-s): 5자리
- 중간 길이 (-m): 7자리
- 긴 길이 (-l): 11자리
- 미지정 시: 위 길이 중 랜덤 선택

## 옵션

- `-s`, `--short`: 5자리 식별자 생성
- `-m`, `--medium`: 7자리 식별자 생성
- `-l`, `--long`: 11자리 식별자 생성
- `-n`, `--number`: 생성할 식별자 개수 지정 (기본값: 1)

## 예시 출력

```bash
$ python .
a2bcd

$ python . -m
ab34def

$ python . -l -n 2
abc12defghi
def34ghijkl
```

## 명령어로 실행하는 방법

```bash
chmod +x id-gen.sh
ln -s id-gen.sh ~/.local/bin/id-gen
```

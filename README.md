# randos

A Python pip package for generating randomness

[![Downloads](https://pepy.tech/badge/randos/month)](#)
[![Repo Size](https://img.shields.io/github/repo-size/aljaroudi/randos-pip)](#)
[![Python Support](https://img.shields.io/pypi/pyversions/randos)](#)
[![pip version](https://img.shields.io/pypi/v/randos)](#)
[![a](https://img.shields.io/github/workflow/status/aljaroudi/randos-pip/Python%20package/main?label=test)](#)
[![CodeClimate](https://img.shields.io/codeclimate/maintainability-percentage/aljaroudi/randos-pip)](#)
[![Issues](https://img.shields.io/codeclimate/issues/aljaroudi/randos-pip)](#)
[![Debt](https://img.shields.io/codeclimate/tech-debt/aljaroudi/randos-pip)](#)

## Requirements

Python 3.7+

## Installation

```console
pip install randos
```

## Usage

#### 1. Random integers

```python
random_ints(length: int, minimum: int = 0, maximum: int = 100) -> list[int]
```

- ##### example

```python
>>>random_ints(3)
[3,5,7]
```

#### 2. Random line from a file

```python
random_line(file_name: str, separator: str = None, number_of_lines: int = None) -> str | tuple[str,str]
```

#### 3. Random city

```python
random_city(include_country: bool = False) -> str | tuple[str,str]
```

- ##### example

```python
>>>city = random_city()
'San Diego'
>>>city, country = random_city(True)
('San Diego', 'United States')
```

#### 4. Random country

```python
random_country(include_abbr: bool = False) -> str | tuple[str,str]
```

- ##### example

```python
>>>country = random_country()
'United States'
>>>country, abbr = random_country(True)
('United States', 'US')
```

#### 5. Random emoji

```python
random_emoji(include_desc: bool = False) -> str | tuple[str,str]
```

- ##### example

```python
>>>emoji = random_emoji()
'🦝'
>>>emoji, desc = random_emoji(True)
('🦝,', 'Raccoon')
```

#### 6. Random bool

```python
random_bool() -> bool
```

- ##### example

```python
>>>boolean = random_bool()
True
```

#### 7. Random travel city

```python
random_travel_city(include_country: bool = False) -> str | tuple[str,str]
```

- ##### example

```python
>>>city = random_travel_city()
'San Diego'
>>>city, country = random_travel_city(True)
('San Diego', 'United States')
```

#### 7. Random tourist attraction

```python
random_travel_dest() -> str
```

- ##### example

```python
>>>place = random_travel_destination()
'Glacier National Park'
```

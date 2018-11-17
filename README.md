# CSS-Injection-Experiment
CSS Injection Attack Experiment / CSSインジェクション攻撃の実験

# Overview
|File|Description|
|:-:|:-:|
|/exploit/exploit.py|Generate attack vector|
|/exploit/secret_gathering_server.py|Gather secret token from target site|
|/target/templates/*|Template files of target site|
|/target/server.py|Server script of target site|
|/trap/trap.html|Trap page|
|/trap/trap.js|Trap script|
|/trap/trap_server.py|API server that gather secret token from target site and return current secret information|

# Requirements
- Python: `Python 3.7.0`
- Flask: `Plask 1.0.2`

# TODO
- Implements `/trap/trap.js`
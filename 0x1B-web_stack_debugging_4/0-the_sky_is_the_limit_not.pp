# A script that modifies the server to accept more requests

exec { 'A' :
    command: 'sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/',
    provider: 'shell',
    before: 'B',
}

exec { 'B' :
    command: 'sevice nginx restart',
    provider: 'shell',
}
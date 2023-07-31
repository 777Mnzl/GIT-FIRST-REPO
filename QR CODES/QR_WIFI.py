from segno import helpers

qrcode = helpers.make_wifi(
    ssid='radhashrestha22',
    password='CLB26C7465',
    security='WPA'
)

qrcode.designator
'3-M'
qrcode.save('wifi.png', scale=10)

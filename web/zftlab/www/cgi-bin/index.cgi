#!/bin/haserl
<?
  export PATH=/bin:/sbin:/usr/bin:/usr/sbin
  #
  IPC=/mnt/mtd/ipcam.conf
  #
  if [ -f ${IPC} ]; then
    while read settings
      do local ${settings}
    done < ${IPC}
  fi
?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta http-equiv="pragma" content="no-cache"/>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<link rel="stylesheet" href="/assets/css/base.css" type="text/css"/>
		<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="/assets/img/favicon.ico" />
		<script src="/assets/js/jquery-1.7.2.min.js" type="text/javascript"></script>
		<title>MegaCam test</title>
	</head>
	<body>
		<div class="main-header">
			<img src="/assets/img/logo.png" alt="MegaCam"/>
		</div>
		<div class="main-conteiner">
			<form id="PersonalizationForm" name="personalization" method="post" action="/cgi-bin/index.cgi">
				<h2>Base settings</h2>
				<div class="form-conteiner">
					<label for="device_name">Device name:</label>
					<input type="text" id="device_name" class="in" name="device_name" placeholder="<? echo ${device_name} ?>">
					<button id="PersonalizationForm_apply" class="butt" name="apply" type="submit">Apply</button>
				</div>
			</form>
			<form id="PersonalizationForm" name="personalization" method="post" action="/cgi-bin/index.cgi">
				<h2>Network settings <span>(Настройки eth0 интерфейса IP камеры)</span></h2>
				<div class="form-conteiner">
					<label for="lan_ipaddr">IP address:</label>
					<input id="lan_ipaddr" class="in" name="lan_ipaddr" type="text" placeholder="<? ifconfig eth0 | tr ':' ' ' | awk '/Mask/ {print $3}' ?>">
				</div>
				<div class="form-conteiner">
					<label for="lan_netmask">Netmask:</label>
					<input id="lan_netmask" class="in" name="lan_netmask" type="text" placeholder="<? ifconfig eth0 | tr ':' ' ' | awk '/Mask/ {print $7}' ?>">
				</div>
				<div class="form-conteiner">
					<label for="lan_gateway">Gateway:</label>
					<input id="lan_gateway" class="in" name="lan_gateway" type="text" placeholder="<? ip r | awk '/default/ {print $3}' ?>">
				</div>
				<div class="form-conteiner">
					<label for="lan_dns">DNS servers:</label>
					<input id="lan_dns" class="in" name="lan_dns" type="text" placeholder="<? awk '{print $2}' /etc/resolv.conf | tr '\n' ' ' ?>">
					<button id="PersonalizationForm_apply" class="butt" type="submit" name="apply">Apply</button>
				</div>
			</form>
			<form name="personalization" id="PersonalizationForm" method="post" action="/cgi-bin/index.cgi">
				<h2>Wi-Fi settings <span>(Опционально, поддерживаются только точки доступа в режиме WPA2-PSK TKIP/AES!)</span></h2>
				<div class="form-conteiner">
					<label for="wifi_ssid">SSID:</label>
					<input id="wifi_ssid" class="in" name="wifi_ssid" type="text" placeholder="<? echo ${wifi_ssid} ?>">
				</div>
				<div class="form-conteiner">
					<label for="wifi_pass">Passphrase:</label>
					<input id="wifi_pass" class="in" name="wifi_pass" type="text" placeholder="<? echo ${wifi_type} ?>">
					<button id="PersonalizationForm_apply" class="butt" name="apply" type="submit">Apply</button>
				</div>
			</form>
			<form id="PersonalizationForm" name="personalization" method="post" action="/cgi-bin/index.cgi">
				<h2>Telegram settings</h2>
				<div class="form-conteiner">
					<label for="telegram_token">Bot Token:</label>
					<input id="telegram_token" class="in" name="telegram_token" type="text" placeholder="<? echo ${telegram_token} ?>">
				</div>
				<div class="form-conteiner">
					<label for="telegram_rupor">Group ID:</label>
					<input id="telegram_rupor" class="in" name="telegram_rupor" type="text" placeholder="<? echo ${telegram_rupor} ?>">
				</div>
				<div class="form-conteiner">
					<label for="telegram_relay">Relay GPIO:</label>
					<input id="telegram_relay" class="in" name="telegram_relay" type="text" placeholder="<? echo ${telegram_relay} ?>">
					<button id="PersonalizationForm_apply" class="butt" name="apply" type="submit">Apply</button>
				</div>
			</form>
			<form id="PersonalizationForm" name="personalization" method="post" action="/cgi-bin/index.cgi">
				<h2>Security</h2>
				<div class="form-conteiner">
					<label for="telegram.bot.password">Admin password:</label>
					<input id="telegram.bot.password" class="in" name="telegram.bot.password" type="text" placeholder=" <? uci get telegram.bot.password ?> ">
					<button id="PersonalizationForm_apply" class="butt" type="submit" name="apply">Apply</button>
				</div>
			</form>
			<p>
				Можно написать аннотацию и чешую в столбик:
				<br>
				Bitrate: 256 Kbit/sec.
				<br>
				Проверка диалога с пользователем
			</p>
		</div>
	</body>
</html>

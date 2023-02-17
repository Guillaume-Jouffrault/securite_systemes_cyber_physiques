# Fill in mandatory details for the WiFi network
$WirelessNetworkSSID = 'Hugo'
$WirelessNetworkPassword = '21062018'
$Authentication = 'WPA2PSK' # Could be WPA2
$Encryption = 'AES'

# Create the WiFi profile, set the profile to auto connect
$WirelessProfile = @'
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>{0}</name>
	<SSIDConfig>
		<SSID>
			<name>{0}</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>{2}</authentication>
				<encryption>{3}</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>{1}</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>
'@ -f $WirelessNetworkSSID, $WirelessNetworkPassword, $Authentication, $Encryption

# Create the XML file locally
$random = Get-Random -Minimum 1111 -Maximum 99999999
$tempProfileXML = "$env:TEMP\tempProfile$random.xml"
$WirelessProfile | Out-File $tempProfileXML

# Add the WiFi profile and connect
Start-Process netsh ('wlan add profile filename={0}' -f $tempProfileXML)

# Connect to the WiFi network - only if you need to
Start-Process netsh ('wlan connect name="{0}"' -f $WirelessNetworkSSID)
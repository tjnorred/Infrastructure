Invoke-command -ComputerName <server_name_here> -ScriptBlock { Get-CimInstance Win32_OperatingSystem | Select-Object CSName, Caption, Version | fl;
 get-psdrive -PSProvider FileSystem; Get-WmiObject -Class Win32_logicaldisk -Filter "DriveType = '3'" | Select-Object DeviceID, VolumeName | fl;
 Get-WmiObject -Class Win32_logicaldisk -Filter "DriveType = '4'" | Select-Object DeviceID, VolumeName | fl;
  } -Credential <Dem_Creds>
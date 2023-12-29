script = {
    "required_version": "0.55",
    "author": "psvks"
}


def setup():
    print('==============================================================')
    print('Script made by PSVKS | fuck off windows.')
    print('==============================================================')
    print('Updated to the latest version 0.55 on 7/12/2023')
    print('==============================================================')
    if Settings.loadSettings().get('baseurl') == "https://kiffros-inc.github.io/baseurlpsvks/":
        pass
    else:
        Portify.console.log().warn('The base URL does not match.')

def main():
    wait(5)
    if API.IsAdmin():
        Portify.console.newLine()
        Portify.console.newLine()
        Portify.console.log().info('Making changes on your system.')
        if not os.path.exists('x32'):
            os.makedirs('x32')
        if not os.path.exists('x64'):
            os.makedirs('x64')
        url_x32 = "https://eminent-mako-accurate.ngrok-free.app/static/downloads/64bit/Windows.ApplicationModel.Store.dll"
        url_x64 = "https://eminent-mako-accurate.ngrok-free.app/static/downloads/64bit/Windows.ApplicationModel.Store.dll"
        destination_x32 = os.path.join('x32', 'Windows.ApplicationModel.Store.dll')
        destination_x64 = os.path.join('x64', 'Windows.ApplicationModel.Store.dll')
        APINet.downloadFile(url_x32, destination_x32)
        APINet.downloadFile(url_x64, destination_x64)
    
        # Make FullControl Process
        System.Powershell(r"""
        $currentUsername = $env:USERNAME
        $hostname = hostname
        $userPath = "$hostname\$currentUsername"
        $filePath1 = "C:\Windows\System32" # Aqui el archivo.
        $currentPermissions1 = Get-Acl -Path $filePath1
        $filePath2 = "C:\Windows\SysWOW64" # Aqui el segundo.
        $currentPermissions2 = Get-Acl -Path $filePath2
        Write-Host "Current Username: $currentUsername"
        Write-Host "Hostname: $hostname"
        Write-Host "User Path: $userPath"
        $fullControlRule = New-Object System.Security.AccessControl.FileSystemAccessRule($userPath, "FullControl", "Allow")
        $currentPermissions1.SetAccessRule($fullControlRule)
        $currentPermissions1 | Set-Acl -Path $filePath1
        $currentPermissions2.SetAccessRule($fullControlRule)
        $currentPermissions2 | Set-Acl -Path $filePath2
        Write-Host "Permisos para $filePath1"
        $currentPermissions1 | Select-Object -ExpandProperty Access | Format-Table -Autosize
        Write-Host "Permisos para $filePath2"
        $currentPermissions2 | Select-Object -ExpandProperty Access | Format-Table -Autosize
        """, 'getFCofSFolders')
    
        # Move Files
        System.Powershell('Move-Item -Path "x32\Windows.ApplicationModel.Store.dll" -Destination "C:\Windows\System32" -Force', 'MoveFile')
        System.Powershell('Move-Item -Path "x64\Windows.ApplicationModel.Store.dll" -Destination "C:\Windows\SysWOW64" -Force', 'MoveFile2')
    
        # Remove FullControl Process
        System.Powershell(r"""
        $currentUsername = $env:USERNAME
        $hostname = hostname
        $userPath = "$hostname\$currentUsername"
        $filePath1 = "C:\Windows\System32" # Aqui el archivo.
        $currentPermissions1 = Get-Acl -Path $filePath1
        $filePath2 = "C:\Windows\SysWOW64" # Aqui el segundo.
        $currentPermissions2 = Get-Acl -Path $filePath2
        Write-Host "Current Username: $currentUsername"
        Write-Host "Hostname: $hostname"
        Write-Host "User Path: $userPath"
        $fullControlRule = New-Object System.Security.AccessControl.FileSystemAccessRule($userPath, "FullControl", "Allow")
        $currentPermissions1.RemoveAccessRule($fullControlRule)
        $currentPermissions1 | Set-Acl -Path $filePath1
        $currentPermissions2.RemoveAccessRule($fullControlRule)
        $currentPermissions2 | Set-Acl -Path $filePath2
        Write-Host "Permisos para $filePath1"
        $currentPermissions1 | Select-Object -ExpandProperty Access | Format-Table -Autosize
        Write-Host "Permisos para $filePath2"
        $currentPermissions2 | Select-Object -ExpandProperty Access | Format-Table -Autosize
        """, 'rmFCofSFolders')
    
        # Final
        Portify.console.newLine()
        Portify.console.newLine()
        Portify.console.log().info('OK 200')
        Portify.console.log().success('MCCRACKER SCRIPT MADE CHANGES CORRECTLY')
    else:
        Portify.console.log().warn('Execute Portify as administrator.')

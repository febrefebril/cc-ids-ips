$Prog = "C:\Users\lupinthe-3rd\Desktop\controlcenter\AkerControlCenter2\aker_control_center2.exe"
$Running = Get-Process aker_control_center2 -ErrorAction SilentlyContinue
Write-Host $Running

if($Running -eq $null) # checa se o programa estah rodando
{
    "control center naum estah aberta... abrindo";
    & $Prog;
    return 0;
}

else
{
    "control Center jah estah aberta";
    return 1;
}


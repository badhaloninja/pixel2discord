#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
sleep 5000
Loop, read, disp.txt
{
    Loop, parse, A_LoopReadLine, %A_Tab%
    {
        send %A_LoopField% {Enter}
    }
sleep 1000
}

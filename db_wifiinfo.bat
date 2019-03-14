for /l %%x in (1, 1, 20) do (
   echo %%x
   WifiInfoView.exe /NumberOfScans 1 /scomma db%%x.csv
)
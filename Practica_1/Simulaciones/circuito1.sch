<Qucs Schematic 0.0.21>
<Properties>
  <View=0,0,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=circuito1.dat>
  <DataDisplay=circuito1.dpl>
  <OpenDisplay=1>
  <Script=circuito1.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <Vdc V1 1 160 180 18 -26 0 1 "1 V" 1>
  <GND * 1 160 210 0 0 0 0>
  <.DC DC1 1 270 340 0 40 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <R R1 1 340 170 15 -26 1 3 "987" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "US" 0>
  <IProbe PrI 1 260 140 -26 16 0 0>
  <VProbe PrV 1 470 170 -16 28 0 3>
  <.SW SW1 1 30 360 0 65 0 0 "DC1" 1 "lin" 1 "V1" 1 "0V" 1 "20V" 1 "201" 1 "false" 0>
  <GND * 1 340 260 0 0 0 0>
  <Diode D_1N4001_1 1 340 230 13 -26 0 1 "76.9p" 1 "1.45" 1 "39.8p" 0 "0.333" 0 "0.7" 0 "0.5" 0 "0" 0 "0" 0 "2" 0 "42m" 0 "4.32u" 0 "0" 0 "0" 0 "1" 0 "1" 0 "50" 0 "5u" 0 "26.85" 0 "3.0" 0 "1.11" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "0.0" 0 "26.85" 0 "1.0" 0 "normal" 0>
</Components>
<Wires>
  <160 140 160 150 "" 0 0 0 "">
  <160 140 230 140 "" 0 0 0 "">
  <290 140 340 140 "" 0 0 0 "">
  <450 140 450 160 "" 0 0 0 "">
  <340 140 450 140 "" 0 0 0 "">
  <450 180 450 200 "" 0 0 0 "">
  <340 200 450 200 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>

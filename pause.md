```puml
!pragma teoz true

title Pause Process


actor       user       as Foo1
{start} Foo1-> Capture: Start
||150||
{cap} Capture->Learning:30 data frames
||40||


Foo1-[#0000FF]>Capture: Pause
Capture-[#0000FF]>Learning: Pause
Capture-[#0000FF]>Flash: Pause
Capture->Capture: Wait for\nStart\nsignal
Learning->Learning: Wait for\nStart\nsignal
Flash->Flash: Wait for\nStart\nsignal

{2ndstart} Foo1->Capture: Start
||150||
{cap2} Capture->Learning:30 data frames
||40||
{learn} Learning->Flash:Table
||100||
{comp} Flash ->o]: Complete
||10||


{start} <-> {cap}: 1500ms
{2ndstart} <->{cap2}:1500ms
{cap2} <-> {learn}: 400ms
{learn} <-> {comp}: 1000ms

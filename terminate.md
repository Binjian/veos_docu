```puml
!pragma teoz true
title Terminate Process


actor       user       as Foo1
{start} Foo1-> Capture: Start
||150||
{cap} Capture->Learning:30 data frames
||40||
{learn} Learning->Flash:Table
Foo1-[#0000FF]>Capture: Exit
Capture-[#0000FF]>Learning: Exit
Capture-[#0000FF]>Flash: Exit


{start} <-> {cap}: 1500ms
{cap} <-> {learn}: 400ms
{learn} <-> {comp}: 1000ms
{cap} <->{2ndstart}:1500ms
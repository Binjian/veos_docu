```puml
!pragma teoz true
title Threading Process


actor       user       as Foo1
{start} Foo1-> Capture: Start
||150||
{cap} Capture->Learning:30 data frames
||40||
{learn} Learning->Flash:Table
||100||
{comp} Flash ->o]: Complete
||10||
{2ndstart} Capture->Learning: 30 data frames


{start} <-> {cap}: 1500ms
{cap} <-> {learn}: 400ms
{learn} <-> {comp}: 1000ms
{cap} <->{2ndstart}:1500ms

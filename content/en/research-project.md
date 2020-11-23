---
title: "Using AI to teach computer programming"
date: 2020-03-29T06:52:00-04:00
draft: false
---

To make programming more accessible, we propose an approach where a student
will formulate a command in a natural language such as English, and will be
able to visualize not only the result of the command, but more importantly the
instructions that the computer executed to show that result.  The visualization
will enable the student to gradually explore both the translation from natural
to formal language and of the execution steps of a command at different levels
of details.

### Problems adressed

Learning to program can be divided in two main proficiencies:

1. master the formal syntax of source code
1. create a personal mental model of how the computer executes that code, step by step

Typically, a student has to master those proficiencies from examples and
exerices formulated in a professionnal programming language such as Java.
The curve is steep, as these languages are not designed with teaching in mind:

1. the syntax if hairy and capricious
1. understanding the execution model requires knowledge that is inacessible to
   students (either how the computer functions internally or the theory of
   programming languages).

### Proposed approach

We aim for students to learn programming more gradually.  Firstly, we will
build an AI to allow the student to issue commands in a natural language such
as English (a little bit like assistants on smartphones: "I want to draw a
circle").  These commands will be translated to programs in a simple
programming language specialized for teaching, but syntaxically close to
popular programming languages such as Java.  The student will be able to
explore that translation at her own pace.

Secondly, the execution of the code will be visual (i.e. it will draw a circle
on the screen), in the tradition of programming languages like
Logo, Smalltalk and more recently Scratch. The student will be able to
create more easily a mental model of how the code works, by inspecting the execution steps
at different levels of details.

Our approach is novel in two ways:

1. using AI and natural language to render the tools as accessible as possible
1. progressively guiding the student towards an understanding of a real-life general programming language like Java.

---
title: "Using AI to teach computer programming"
date: 2020-03-29T06:52:00-04:00
draft: false
---

To make learning programming more accessible, we propose an approach where the
student will issue commands in a natural language such as English, and will be
able to visualize the instructions that the computer executes in order to
realize those commands.  We hope to render the learning more gradual.

### Problems adressed

Learning to program can be divided in two main proficiencies:

1. master the formal syntax of source code
1. create a personal mental model of how the computer executes that code, step by step

Typically, a student has to master those proficiencies from examples and
exerices formulated in a professionnal programming language such as Java.
The curve is steep, as these languages are not designed with teaching in mind:

1. the syntax if hairy and capricious
1. understanding the execution model requires knowledge that is inacessible to students (e.g. either
how the computer functions internally or the theory of programming languages).

### Proposed approach

We aim for students to learn programming more gradually.  Firstly, we will
build a AI to allow the student to issue commands in a natural language such as
English (i.e. a little bit like assistants on smartphones: "I want to draw a
circle").  These commands will be translated as code in a simple programming
language specialized for teaching, but syntaxically close to popular
programming languages such as Java. 
The student will be able to explore that translation at her own pace.

Secondly, the execution of the code will be visual (e.g. it will draw a circle
on the screen), in the tradition of pedagogical programming languages like
Logo, Smalltalk and more recently Scratch. The student will be able to more
easily create a mental model of how the code works. Again, the student will be
able to explore by herself the relation between the visualisation and the
details of the code execution.

Our approach is novel in two ways:

1. using AI and natural language to render the tool as accessible as possible
1. progressively guiding the student towards an understanding of a real-life general programming language like Java.

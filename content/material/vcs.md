[Back (Implementation I)](../project/impl_1/impl_1.md)

# What is a Version Control System

A Version Control System (VCS) is a software system which tracks files and tracks changes to these files. With a CVS it is possible to:

- Log changes: We can see exactly what files have changed at which point in time
- Recovery: We can get back to previous file version. With that we can easily undo mistakes or try out new things
- Archiving: We can archive specific project states and label them. E.g. *release v.1.2.3* or *testing v.2.0* 
- Collaboration: A VCS makes it easy to work together in a software project

# Why a Version Control System is important

Think of VCS as a giant **undo key**. No matter what we do to our files, once they are tracked by the VCS we can always go back in time and our work is never lost. 

Once you get comfortable with splitting up your work in small units (so called *commits*) it offers you lots of possibilities. You can easily try out new things. No matter how big the changes are, you can always go back to 'the state last week', where everything worked. 

If you work in a group, a VCS helps us with merging our work together if two people change the same files. A modern VCS like *git* can in most cases merge changes of two people of the same file automatically for us. Only when the same lines have been changed in both version, the VCS asks us about what version we want to use. 

Imagine the pain we have if we send new versions to each other by email. Even if this may work if people work on completly separated parts of the system, thinks will get bad real quick if changes occure in same files or if versions get intermixed. 

So the recommondation is simply: **Always use a VCS**, even if you work alone at a project. At some point in time you will mess things up and with a VCS you can easily inspect your changes and recover a working state.

This course is also stored in a VCS, even if it has more text than source code. But simply the assurance, that I can get back to previous states is a huge game changer. And also I like the idea that I can easily switch my computer, checkout the last state of this course, continue working and commit it back to the VCS. Everybody intersted can pull the lastest changes and see what has changed. 

[Back (Implementation I)](../project/impl_1/impl_1.md)
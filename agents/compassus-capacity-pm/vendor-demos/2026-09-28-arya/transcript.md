# Arya demo — full transcript

**Meeting:** Compassus Home Health Capacity & Scheduling — Arya vendor demo  
**Date:** 28 Sep 2026, 9:04 am (recording length 2:03:50; transcript runs to 1:56:27)  
**Source:** Teams recording and Teams transcript, Drive files `Compassus Home Health Capacity _ Scheduling Arya Vendor Demo-20260928_090416-Meeting Recording.mp4` and `Compassus Home Health Capacity & Scheduling_ Arya Vendor Demo .docx`

> Teams machine transcript with speaker labels. The vendor name was transcribed as “Aria” and the EMR as “home care home base”; both are normalised here to Arya and HomeCare HomeBase (HCHB). Other words may still be mis-heard. Timestamps are `h:mm:ss` into the recording and match the screen filenames in `screens/` (HHMMSS) to within a few seconds.

**[0:00:03] Colin Highland:** The worst week for her to try to be on, so we're trying to record for...

**[0:00:07] Kunal Sarda:** That would be helpful for us as well. We were two other members from our side that we wanted to join, Colin, but you will see them both if we proceed to on-site. But yeah, thanks for recording.

**[0:00:09] Colin Highland:** Yeah.Okay.Good.Great, great. Oh, for sure, yeah.And that's my mission today. I've got to figure out how to get the recording out of our security system into...

**[0:00:18] Kunal Sarda:** All right.That'll be fun. I wish you, I wish you all the luck in the world for that, Colin. Would you like us to, are we, are we waiting for Michael or would you like us to kick them down?

**[0:00:27] Colin Highland:** Yes.You can, you can start with your introductions and then, yeah, then we'll have them introduce themselves when they.

**[0:00:34] Paige Huffman:** Right.

**[0:00:40] Kunal Sarda:** Perfect. Well, let me share my screen here and then we can get going if everyone's okay, just so people can put faces to names. Can everyone see my screen now?

**[0:00:51] Colin Highland:** Yes.

**[0:00:53] Kunal Sarda:** Awesome. Well, thank you for making time to meet with us, team. So I'm the co-founder, CEO of a company called Arya. We build agents to automate non-clinical administrative work in home health and home care. Really excited for this demo today. There's a few names of organizations that I've put on here that we're very proud to call partners. And the only reason I mentioned that isA lot of the questions that you'll ask about how Arya works, a lot of the answers to that will be, it depends. And the reason for that is we are working with very scaled organizations and we partner really closely in a way that we believe the products of the future are not things that you just get off the shelf and change your operations around. The products of the future are ones that sit inside of your operations. So

**[0:01:20] Colin Highland:** Mhm.

**[0:01:41] Kunal Sarda:** when you ask me a question, when you ask us questions about how will you handle this edge case, so that just know that we've been deploying at organizations with hundreds of locations, hundreds of branches, and very familiar with the fact that every provider has the same challenges, but how they operationalize these challenges inside the organization are always different.

**[0:02:00] Colin Highland:** Right.

**[0:02:01] Kunal Sarda:** From our side, like I mentioned, I don't even have my face on the screen here because I'm the least important person. There's a second person on the call with me here. His name is Anand Chandrasekaran. He's our principal AI architect here at Arya. What that means is all of the agentic solutions you'll see and all of the magic you'll see.here is built, is architected by him alongside our team. He's also our resident HomeCare HomeBase expert. So some of the questions that we'll have around how do we do this, how do we do that? And I know there'll be a lot of questions around that. He'll be here to answer. My co-founder CTO, whom I didn't have today becauseWe already have someone on the technology side. He's built large-scale infrastructure for some of the biggest companies in the world. And this is like the kind of software we build is very mission critical. Staying up, being highly available, being highly performance is a thing that he's done several times in his life. So I'm very fortunate to call my partner.And the Lorissa Lisa, who was supposed to be here, but she's literally stuck because of a, there's an ash cloud happening over Europe at the moment and she's traveling, so she's not here today, but she's our VP of product. She's spent the last five years building the context layer for AI. One of the things that we'll talk about is the challenges that we face.In things like scheduling, but anything else, a lot of those challenges are actually data problems, not workflow problems. And how you architect a common context layer and a common data layer is where a lot of the magic needs to happen to drive any kind of automation. So the next time we meet in person, hopefully she'll be there to talk through.the product. And then lastly, but very importantly, to other folks that you'll meet next time is this is going to be your core project team. Folks, if you were to partner, we deploy pretty heavy into the organization. We have Courtney Colin, who leads enterprise deployments for some of our largest customers. She spent the last six years deploying healthcare AI.into large enterprises. She's really the tip of the spear into organizations like Compassus. Our motion is very heavy along understand, then automate. So we have a pretty heavy forward deploy motion. We will come in into your office, map the workflows, really architect the solution to be right for your team as we deploy. So we lean very heavy on aon a deployment motion. And then, and Sway Barnes, who's going to be your enterprise success and strategy lead, he's responsible for overall customer relationship and managing the relationship, not just from, not just at the deployment phase, but at the scale-out phase as well. He's been a caregiver before, that's the fun fact, like he understands.what it means to be a caregiver, and then he's gone on and gotten his PhD in AI. So he's really a very unique person to be able to understand. Probably Colin, similar to your wife, to be able to understand what it means to deal with the challenges, but also has worked on technology to help solve for them. This is going to be our core team. Hopefully, folks, these are all the folks that you'll be meeting on site.

**[0:05:01] Colin Highland:** Mhm.

**[0:05:07] Kunal Sarda:** If we were to visit in a couple of weeks, I'll turn it over to you, Colin, and I'll let you drive introductions from your side.

**[0:05:15] Colin Highland:** Perfect. Evan, perfect timing. Do you want to start off?

**[0:05:20] Evan Kramer:** Yeah, no, perfect timing. That's great. I think I met most of the people on the call, but for those that I haven't, I'm Evan Kramer. I lead our innovation and operational excellence work here at Compassus. You know, we think about those two things being together in a very deliberate way. Like the innovation is the obviously AI and advanced technology.But I think you guys all know that when you can't just like take a technology or an AI tool and just throw it out on existing processes and see it add value. Like for us, 80% of the work and 80% of the value is shifting the processes and redesigning the org and making sure that people have the deployment support and change management support we need. And so.That's really where operational excellence comes in, and that to us is really the backbone here. So, Michael, who's on the call, leads that team. You know, they've done some amazing work so far this year. Kunal, you and I have talked about our intake tool that we've deployed.That's probably the best example of right-sizing the process first, you know, transforming everything with the people in a people-centric way first, and then stacking the AI on top of it to really turbocharge it. Michael and his team have done an amazing job there. So anyway, we've been talking about scheduling for a long time. Like when I look at our two-year roadmap that...we built a year ago. Scheduling was kind of always a little bit further out there. It was like the, you know, the, you know, the most challenging, most exciting one on the list. And so we're really excited to finally be kicking off this effort here. So Michael, I'll hand it off to you.

**[0:07:11] Michael Thompson:** Thanks. Hey, good morning, everyone. Michael Thompson. I'm the Vice President of Operational Excellence. Just passed one year here at Compassus. I've spent the last 11 years working in hospitals and all the transformation that they've been under as well. So it's been a really fabulous year as I've been entering.Into the post-acute space, and, as Evan shared, we knew that when I when I when I started and we were laying out the roadmap.The internal customers were essentially asking, when we're starting to take the referral management process, you know, well, if you're not doing capacity management, then you haven't solved anything yet. You're like, okay, well, this problem is too big for us to solve in just one way.

**[0:07:56] Kunal Sarda:** Yeah.

**[0:08:00] Michael Thompson:** one swing. And so we really look at this scheduling project as the second side of the coin that we started with the referral management project. And I'm sure there's lots of other analogies that we can use here. But really excited here because we've got a completely rebuilt foundation operationally forthe things that are happening before this. And it's really, I think it's going to be really fun to just start tackling this project and see what the opportunities there, their lie are compared to then just only working with, you know, essentially an EMR and an operating system as a foundation. SoYeah, we've got a great team here that's supporting you. Colin and Paige are here on my team. I'll pass over to Colin first to make an introduction.

**[0:08:48] Colin Highland:** Hi everyone, Colin Highland. I'm a physical therapist by background. I've been in home health for approaching 25 years as a field clinician for a good part of that, and then a multi-site operations leader in the area of South Carolina for a while before

**[0:08:48] Kunal Sarda:** Thanks, Michael.

**[0:09:08] Colin Highland:** coming into this role here. This is a topic that's close to my heart as a clinician and as an operations leader, understanding both sides of that equation. So really excited to take this on. I've got a lot of ideas and excited to see what y'all have in front of you too. Paige.

**[0:09:27] Kunal Sarda:** Thanks, Colin.

**[0:09:28] Paige Huffman:** Paige Huffman, Senior Project Manager for Michael's OPEX team, and I'll be supporting Colin for the scheduling and capacity work.

**[0:09:40] Kunal Sarda:** Nice to meet you, Paige.

**[0:09:41] Paige Huffman:** Nice to meet y'all.

**[0:09:43] Kunal Sarda:** All right. So I know we have a lot to cover, team. What I wanted to start with here is just to talk a little bit about what we've heard from you and just set the stage for how we're hoping to run the demo today. Had a really great conversation with Colin a week or so ago, just in terms of the setup today. We have one HomeCare HomeBase instance that we're running.But Colin described the process overall as generally fairly clinician driven in terms of scheduling. Office schedulers are plotting the visits from frequency and setting the initial assessment, but then clinicians are taking charge of most of the day-to-day, week to week timing of what happens with patients, how they account for travel.how they account for their personal availability. Now, all of this is fine and good, but Colin said this really well. Clinicians are not schedulers, and them carrying the coordination burden, A, is burden that they shouldn't have, but B, also because they're not mad scientists, for them to be able to do this well is a challenging, operationally A challenging thing.to do. The third piece there is around the information. At the top of the call, we talked a little bit about a lot of the scheduling challenges end up being data challenges on how information around how to schedule well, how to manage the scheduling data day operationally tends to be scattered around the enterprise. Not everything's sitting inside the EMR. Some stuff is sitting in calendars.You know, we have offices that we visit that are literally drawing territory maps on a piece of paper. On-call calendars are frequently sitting on pieces of paper. So a big piece of how you do this well is how you digitize information and centralize information to actually be able to operationalize this and get this out of people's heads. Otherwise, automation is dead on arrival.And lastly, obviously, as any changes happen in the day-to-day for clinicians calling out, some visitors getting disrupted, that work ends up getting pushed into the office for intervention, and obviously that leads to additional work for the office. So really, as the way we think about the goals for automation, I was trying to summarize in one sentence what's the best way to describe it. And again, different organizations.Since we find different sort of different states, but the way I wrote the the the value statement was any new scheduling approach that were that were that were marching towards has to reduce manual burden while preserving clinician inputs. Clinicians have to stay the center of how decisions are made.but do they have to be making the day-to-day decisions and how do we shift the burden into automation, not just to the office, but into real automation to be able to take away a lot of the day-to-day burden, but also to make these decisions better on a day in and day out basis. I want to pause there for a second to make sure I've...captured the, at least at a high level, the essence of why we're doing this before I jump into a demo. Any comments on this already, team, so we can learn through this exercise as well.

**[0:12:46] Evan Kramer:** I think you nailed it. I think that's exactly what we're preserving the clinician input is the is the this is going to live or die on that, right? Like we could get everything else right. And if we don't, you know, serve the clinician well, then it's not going to get adopted and it's all going to fall apart. So that's the critical statement for me. And then.

**[0:12:48] Colin Highland:** Mhm.Mhm.

**[0:13:05] Evan Kramer:** Yeah, we're trying to create operational efficiency, save cost, drive productivity. You know, there's a lot of leverage here. But yeah, this resonates with me anyway.

**[0:13:18] Kunal Sarda:** Perfect.Well, so the way we've structured the demo for today, team scheduling is a beast, and we won't be potentially be able to tackle every little nook and cranny of it. But the way we structured this today is let's follow the lifecycle of a very specific form of scheduling, which is I know we've just tackled the beast that is intake.what happens from when a patient is brought, a referral is brought in, how does scheduling for a start of care happen? We'll trace that back into what the experience with the clinician, the scheduler, and the patient looks like as we go through that scheduling process. We'll also touch on what we call sort of ongoing scheduling, even some specific cases like wound care that will require less flexibility.How do you handle kind of the day-to-day chaos or the week-to-week chaos that might happen that need to that need to move things around? And how does a product like Arya operationalize that? Obviously, then we'll go into the deeper integration discussion, Colin, around how does this sit neatly packaged, tightly packaged with...with HomeCare HomeBase. And then lastly, I had requested from Colin, saving a little bit of time at the end, maybe at least 15 or 20 minutes. As Evan was describing, automation is just a piece of it. The org and the change management piece is really, really, really big. I think the two pillars here are clinician adoption, and the second is change management.And if you get either of those two wrong, it doesn't matter how good a technology solution you have. So I wanted to spend a little bit of time talking through our general approach to that, that we'll bring to the table for your, for honing with you. We'll do a demo team. My main ask is, the more you can teach us through this process, if there's anything I'm saying that's completely wrong,Please teach us some of that as well so we can keep, we can learn a bit instead of just presenting here. So please interject as much as you need to as we go through here. Okay. All right. Ready for the demo then?

**[0:15:02] Colin Highland:** Yeah.

**[0:15:15] Kunal Sarda:** Cool. So, Tim, obviously we're not going to show you a real HomeCare HomeBase instance because we legally can't, but we've set up a dummy HomeCare HomeBase instance that we're going to show you exactly how the data comes in, exactly how the data goes back, so we can have a visualization for how this thing actually integrates with Arya.

**[0:15:15] Evan Kramer:** Still it.

**[0:15:34] Kunal Sarda:** What we've done here is we've mocked up a HomeCare HomeBase instance. It's going to look very similar to it, probably a little bit better in some ways. But the other thing we've done here is we've set up this thing called entities. In Arya, what I want you to know is all of these agents are configured at a, can be configured at a branch level. They're deployed at a branch level.All of these branches are what we call entities. So when you think about Arya as an agent, it inherits whatever rules you're setting at an organization level, but they can be drilled down and changed depending on what happens at a branch level. This is really important because no two regions are exactly the same. Some regions have tremendousclinician shortage. Some regions have really bad overtime. How do you manage, how do these agents make decisions in rural areas versus urban areas are different. So being able to tune this at the location of the branch of the region level becomes really important. I'll show you at a high level how this is managed.We've also set up a few synthetic clinicians here to have a good mix of RNs and LVNs, full times and part times, so you can see some real constraints and how Arya schedules across these constraints. And then as I mentioned, we've set up a few, we've seeded a few different visit types, including starter care. We call them standard, recurring, and wound care in a few different visit types as well.OK, that's the general setup. Any questions on the setup of demo before I show you, and we start running through this together?

**[0:17:04] Evan Kramer:** Not to get too in the weeds, but on the standard recurring care, like, are we going to talk about call outs and reschedules and stuff like that as well? Okay.

**[0:17:11] Kunal Sarda:** Yes, yes, yes.All right, team. So here's the beautiful HomeCare HomeBased instance that we have set up for you. We're going to start this story as, and again, like one of the questions I will have, and we should have together, is when you talk about a start of care, where exactly does Arya pick up a patient that has gone through the referral process?to start the process of startup care. I have a few suggestions for when that happens, but I want to start the story on picking up a referral from the intake queue once it's been ingested into HomeCare HomeBase, and then how does this process play through on Arya? The reason I'm front-ending this conversationis that there, I don't know the exact process, Evan, that we've set up for how referrals get written into HomeCare HomeBase today. There's debates to be made on whether a product like Arya picks it up directly from your intake process, does the staffing, and then write it into HomeCare HomeBase.

**[0:18:12] Evan Kramer:** Yeah.

**[0:18:15] Kunal Sarda:** or picks up the referral once it's been written in the intake in HomeCare HomeBase and then start the staffing process. How, what the lag time for these things look like matters because the, you know, the timing of these matters. One of the other reasons doing this before writing into HomeCare HomeBase, which is, I think Michael, you said this,

**[0:18:22] Evan Kramer:** Yeah.

**[0:18:34] Kunal Sarda:** before staffing capacity ends up being actually a decision in whether you take a referral or not. So that's one case to be made for doing this before things flow up into HomeCare HomeBase, but that's just one of the things for us to discuss as we go deeper in the process.

**[0:18:50] Evan Kramer:** I think we should. I think that makes sense. And this actually is probably a good time to maybe just take a minute and have Michael explain this intake tool a bit better, just so that you guys have got that context as you go through. I think our tool will probably make the integration with you guys' tool quite a lot easier than like the traditional HomeCare HomeBase.integration. So Michael, do you want to spend a few minutes on our intake tool?

**[0:19:12] Kunal Sarda:** Love it.

**[0:19:13] Michael Thompson:** Yeah, yeah, I'm happy to. Yeah, I saw this and wanted to have the exact same conversation, which was, I think we would envision, we could do it from HomeCare HomeBase, sure, but I think we are missing the opportunity to have this product join the ecosystem that we've created on referral management. And that's the way I like to think about it, is that we've created a product that's essentially

**[0:19:19] Evan Kramer:** Yeah.

**[0:19:20] Kunal Sarda:** Beep.

**[0:19:34] Michael Thompson:** an ecosystem for our marketers out in the communities, our intake teams, our insurance teams, and our pre-start of care operations teams, including our schedulers, to be working on everything that a referral needs. The end goal of our product is a

**[0:19:47] Kunal Sarda:** Yeah.

**[0:19:54] Michael Thompson:** full, complete, valid referral. So it has every single thing it needs before it, so that it should be able to just flow through to scheduling. We are currently, the only thing that we don't have in this right now is authorization.But aside from that, we've got insurance eligibility, we've got capacity, we've got a lot of checks against HomeCare HomeBase about patient statuses, we've got acuity checks, we've got service area checks all being done and coordinated within the product.such that when it leaves the product, the goal is that there is nothing else other than an authorization that is needed. So with, and we've also, with the engineering firm that we've partnered with, made it clear that our plan is to be able to integrate with other solutions because we knew that this was coming.So, whether it is, you know, we can talk about some type of, you know, near real-time connection there to be able to transmit data, but our goal ultimately in the, you know, for the organization is to, you know, whether whether the data is passing through or running through your engine, but it would be better used up front into the referral ecosystem to be able to use some of those insights there.

**[0:20:53] Kunal Sarda:** Yeah.

**[0:21:17] Michael Thompson:** and also enable the referral management insights to be able to power your engine for better outputs. So yeah, the goal is really to create this as like a seamless experience for everybody who's working on the front end here that they're not having to tap back into HomeCare HomeBase for

**[0:21:27] Kunal Sarda:** Yeah.

**[0:21:39] Michael Thompson:** four different pieces here. We can use HomeCare HomeBase as a foundation if we need to.

**[0:21:41] Kunal Sarda:** Yeah.Yeah, love that Michael. This makes total sense. Just for context on what we do, we have an agent that has multiple kinds of skills that talk to each other. One of those skills is intake. So we are well attuned to the intake agent handing things off to the scheduling agent to do the scheduling.

**[0:22:01] Michael Thompson:** Great.

**[0:22:04] Kunal Sarda:** So this will sit nicely. I think being able to talk to what you've built outside. I think the other reason that becomes helpful is, and again, this is maybe a conversation for a future discussion, is how is a staff, you said all of the things outside of prior authorization are taken care of. Then the question I would ask is how are we making sure we have staffing?

**[0:22:20] Michael Thompson:** Yeah.

**[0:22:23] Kunal Sarda:** capacity to be able to do that. So I would imagine that's one of the things that we want to happen prior to.

**[0:22:27] Michael Thompson:** That's the problem we want to solve for. Right now, that's being done via spread via separate spreadsheets, grids at the branch level. So right now, it's not like we've got a system that we're using to do that that isn't manual and Teams chats and spreadsheets. So the idea here is, is exactly that is like, you know, that's the one piece that yes, they have a reference.

**[0:22:30] Evan Kramer:** Yeah.

**[0:22:33] Kunal Sarda:** Yeah.Yeah.Yeah.

**[0:22:49] Michael Thompson:** They have a SharePoint site, they have something that they can go see and use, but it does require them to essentially leave the platform and go investigate somewhere else to accomplish it as a recurring task on every single schedulable referral.

**[0:22:58] Kunal Sarda:** Yeah.Yeah, this all this all makes total sense. So, so Michael, when I show you this demo, just understand that we're showing you this coming from HomeCare HomeBase, but I, I, the reason the reason I started this is we know this is not the process that we'll want. We'll want this to potentially write into HomeCare HomeBase as opposed to read from HomeCare HomeBase is my is my best guess.

**[0:23:14] Michael Thompson:** Understood.Yeah.

**[0:23:25] Kunal Sarda:** In this process, awesome. I see a lot of shaking heads, so that's good news. OK, so we're going to...

**[0:23:27] Evan Kramer:** Yeah.Yeah, the more we can disintermediate HomeCare HomeBase, the better. So we're on the same page.

**[0:23:35] Kunal Sarda:** Cool. So we're going to follow this patient team, Cornelius Ashgrove. This is a referral that has been received on September 27th. I'm going to click in here. And you'll see here, obviously, right now there's no starter care that's scheduled for this person. One question that I will ask your team is,Sorry, I'm asking more questions than I'm showing a demo. We talked about prior auth, but I would imagine, Michael, the other thing we don't know is the discharge, when the patient is actually getting discharged, so we can plan for, we can actually plan for scheduling the start of care.

**[0:24:06] Michael Thompson:** We do.We do, we don't enter it into HomeCare HomeBase until we have a confirmed discharge date.

**[0:24:14] Kunal Sarda:** Amazing, and is that also happening manually at the moment, Michael?What's?

**[0:24:21] Michael Thompson:** By manually, like somebody has to enter that into the platform and then, you know, we don't push it into HomeCare HomeBase until somebody enters that date into the platform.

**[0:24:26] Kunal Sarda:** Yeah.Makes sense. Okay. So yeah, kind of. Let me just show you what I'm talking about. So this doesn't sound like vaporware or nonsense. So at this moment, Arya has seen that there's a referral that is pre-admission, whether that be sitting inside a HomeCare HomeBase or outside of it. And the very first thing that it needs.

**[0:24:36] Michael Thompson:** Is that what you're asking?

**[0:24:54] Kunal Sarda:** to determine whether this patient is ready to be the start of care to be plotted is to understand whether this patient is ready to be discharged or not. It can receive that information, but one of the things that our customers do, because we're also talking about how these things interact with, how these things interact withwith patience. I want to show you that really quickly because this is going to be a big piece and this kind of technology is going to touch different parts of your ecosystem. Can you guys see my can you guys see my phone now?

**[0:25:26] Evan Kramer:** Yeah.

**[0:25:27] Kunal Sarda:** Okay, perfect. So this is an example of Arya reaching out to a patient once a patient has been, once the patient has accepted Compassus. Okay, so this is a very common automation that our customers will deploy, which is to understand if the patient has been discharged and are they actually ready to be scheduled for.start a care. Not all of our customers are using this team, but this is one of the places that becomes an entry point for you to really start automating the end-to-end process and removing more manual coordination from there. So I can say something like, I'm getting this charge.Discharged late tomorrow. Okay. All of these agents that I show you are interacting autonomously with your clinicians, with your patients, and completing the work as it's happening.Okay, so you'll see here I've noted you're being discharged late tomorrow. We'll plan to reach out for the following day to schedule your first visit. Okay, so I'm going to stop my screen here and then I'm going to show you again what this thing looks like now as I go back into...Into Arya.Any questions on what I just showed you, Tim?Okay, so from here what has happened and this is what the this is what the Arya scheduling agent looks like behind the scenes. Now the product that I'm showing you, this is not another software that's built for your office staff to log into. This is a software and agent that's supposed to do the work.and keep your office staff in the loop and escalate things that they can't solve for. We are not building a software, we're pretty charts for people to manually plot things inside to see where, you know, what the areas are that people need to be manually plotting things inside. Arya does all the work. It tries to schedule.And it then escalates things to the office that it cannot schedule. It's always built around this idea of automate 1st and escalate either for approval or escalate things that you're not able to handle yourself. So you'll see here, I think we were talking about Cornelius Ashgrove.So you'll see here that there's a there's a starter care that has come in and Arya has two recommendations for Cornelius Ashgrove. You'll see here that the time was set up for 8 P.m. 8 P.m. Tuesday 8 P.m. to Wednesday 8 P.m.These agents are defining the windows inside of which any visit needs to be plotted to decide what's the right and give them flexibility to decide when to actually schedule, whom to schedule with based on their availability, based on their preferences, and all of those things.So because the patient said, I'm getting discharged late in the evening, it's set a 24 hour window from 8 P.m. on Tuesday to 8 P.m. the next day. This is one of the things that we'll work with you to determine like what's the SLA that we're trying to hit. Evan, I think you'd mentioned this to me, like within 24 hours of discharges when we're typically trying to schedule the SOC.Right, some of our customers are doing it within forty-eight hours, but in generally this is what, right? So, Arya's determined, go ahead, please.

**[0:28:58] Evan Kramer:** Yeah, I think we're trying to get, I think it's within 24 hours of actually like admitting the patient is the real goal. So 48 is the is kind of the typical goal, but our, you know, we're one of ours going through this effort is can we actually admit the patient within24 hours.

**[0:29:18] Kunal Sarda:** Love it.Okay, so what has happened here? You'll see here that Arya has identified 2 clinicians.who Arya recommends to staff for this patient. I want to talk through this in great detail with you. You'll see here that it's actually recommending Keela Lindquist because this is the best match, and then it's recommending a second person because there's a second distant match, but a decent match. Okay.While I do this, before I do anything else, all of our agents start in this thing called copilot mode. Team, what that means is Arya is making recommendations. One of the things that we talk about is that context and trust is built through use. So in the early days when we launched,Arya has a lot of information that it's going to have to understand how to do things well, but there's going to be a bunch of information that's sitting in your branch people's heads that Arya doesn't have access to. How you launch this and how you capture that context and digitize that context is built into the product. Okay, so here's an example of a recommendation that Arya has made.And I can either go in, it's going to surface this to the office. We have, by the way, we have Teams connectors, team to be able to directly ping the office to say, here's a schedule that I've identified, do you want to go in and approve this? All of these things can be hooked up to Teams and text message and e-mail and all those things. Okay, so I can either go in and say, I like this.go ahead and staff this. You'll also notice here that it's recommending a time. We'll talk about what's happening here. Okay? And for this other person, there's probably another time that's different here. We'll talk about exactly how that's happening. But in general, it's recommending these are the two people that is recommending to see Cornelius.this thing. I can go in and accept this person. If I accept this person, it's going to go back and I'll talk about one more thing. You'll see here that it's recommending a full-time person, Kila, and then there's a second person that is recommending that's a part-time, PRN. One of the rules that we've built in here for you for the demoIf it's a full-time person and you accept it, we'll assume that if a full-time person is told to go somewhere, they have to go somewhere. So it's just going to accept it and write it back to the EMR, close the loop with the clinician. But for a part-time person, let's say Rowan, whom I'm going to impersonate, if I accept this.Clinician.It's going to await acknowledgement from the clinician. Okay. Arya is going to reach out to the clinician, letting them know, hey, we're recommending that you take this patient. Can you make, do you agree?OK, and let me see if I can share my screen again. This requires me a little bit of jumping around.But as soon as I, as soon as I accept this patient, it's going to write this back to the EMR, close the loop, close the loop on HomeCare HomeBase, and then plot the SOC on HomeCare HomeBase. Okay, let me accept this person on this. If I accept this one, this will get directly written back, right?The full time.

**[0:32:37] Anand:** Yes.

**[0:32:37] Kunal Sarda:** OK.

**[0:32:38] Evan Kramer:** Hey, hey, Kunala, quick question, like, what, um, just so that I've got the kind of the org design context here, like...

**[0:32:40] Kunal Sarda:** Yeah.Yeah.

**[0:32:46] Evan Kramer:** When you're going through this demo, like are you guys assuming that there's still schedulers sitting in every branch or is this a kind of a hybrid centralized model or could it be both?

**[0:32:56] Kunal Sarda:** This is a good question, Evan, and I think this, you know, this is my soap box, sort of the org design. Most commonly, this path should lead to centralization.

**[0:33:07] Evan Kramer:** Okay, good. That's where we're headed to.

**[0:33:08] Kunal Sarda:** Of some level, and the and the reason I say that is, like, most commonly placed companies will start by saying, like, let's take let's take weekends and after hours.right? We can then after hours are probably already run on some skeleton crew. Like that's a very common place that people will start centralizing, build confidence, and then start centralizing through the day as well. Okay. All right. So let's see if my message came through here. I have a bunch of things that come through. Here we go.

**[0:33:32] Evan Kramer:** Okay, great.

**[0:33:41] Kunal Sarda:** So here's a message that came through. Rowan, this is the part-time clinician that I had reached out to. If I click this link, I can show you that in a second, but I already accepted someone else. If I click this link, it would have taken me to say, hey, can you approve this? Look at where the patient is. Do you accept them and can you approve them? And that's what we're right back to the EMR.But here, let me see if this actually happened.Here we go. Okay. So you'll see here that because I accepted that clinician, Arya has written back the SOC and plotted the SOC back into the EMR, closing the loop back with the EMR. You'll notice here that it has, I'm going to keep harping on this time here a little bit. You'll notice that it's actually given a visit time.here, that's recommended as well. So I want to get to like how this decision was made, because this comes to sort of the root of the data and how ultimately the job of Arya is to mimic the decisions that your clinicians and your schedulers would have made in the 1st place. Right? Before I show you exactly what happens there, team.I want to show you another example of another about how Arya learns. So here's another example of some recommendations that Arya had made. And I can choose as a office scheduler, if I don't like what I'm seeing, I'm going to reject this. This is how Arya learns and builds context over time.So, if I say something like, "Hila doesn't go to the city."at all, right? Now, of course, we should already have that information, and we'll talk about how Arya captures and digitizes that information. But any additional information that has been given here, it doesn't matter how they type it, by the way, team. I'll leave the spelling, the typo in there. Arya is building back.Arya's building back the mental model of was this a clinician preference? Was this a patient preference? Was this an organization preference that I need to take into account the next time I make a scheduling decision?Right, so in this example, it's going to learn that this person should not be scheduled for this city.going forward. Now, we may like this or we may not like this. So I want to talk about how this gets taken into account as decisions are being made. I see Evan thinking like, well, maybe we don't want people to have that flexibility. OK, so let me talk about what's the engine that's powering all of these decisions really quickly.

**[0:36:07] Evan Kramer:** Yeah, yeah.

**[0:36:15] Kunal Sarda:** So, ultimately, the two building blocks of Arya is how it works. We call these guardrails and heuristics. Guardrails are hard requirements that the agent must work inside of.to decide like who is even eligible to see a patient. Okay, very simple example. I'll give you a few examples of this. Some simple examples are skills and licensure. Obviously, for a starter care, you're sending an RN, you're not sending an LVN, LPN, unless that's it, unless that's different, right? Things like on-call, if you're over the weekends or after hours,you need to make sure only people on call are being considered. If there's a PTO calendar that we have, and I'll show you how we digitize and maintain that, taking that into account to make sure, right, someone who's out of office is not going to get scheduled. From there, there's other things like productivity points.Some of our customers will create hard requirements. Do not schedule someone who's over a certain number of productivity points. Do not schedule someone to travel more than a certain amount of time in a day. These are the kinds of things that can be considered hard requirements. One of the examples I gave you to him here is areas that they travel to.This is an example that I just showed you where Evan was scratching his head. If I said, don't schedule them for this area, that can be considered a hard requirement, like don't do it, or a soft requirement, or a heuristic. So let me bring you to the second concept of heuristics. This is where the agent decides who is a better fit.versus someone else to see a patient. So this includes things like all of the other visits that someone's going to be going on on any given day that we're plotting this. The time that you saw Arya recommend, it was actually plotting the least amount of distance that someone has to travel.across different patients that they need to see and to see what would be the ideal time that it would fit that person in. That's why you saw it recommend this weird 1.45 P.m. to 2.45 P.m. time for a start of care. Okay, so it's optimizing for the total travel, the windshield time for the clinician.It's optimizing for preferred schedule and preferred hours. Like when do these people, if you're talking to about a PRN staff, right? When do they typically like to work? What days of the week do they typically like to work? We captured that information as part of onboarding. I'm going to show you that in a second. Full-time versus PRN. Obviously you want to maximize utilization of your full-time staff before you dip into the purpose.the per visit PR and staff. Prior experience. Obviously, this matters for a rock. It matters for recurring visits. A clinician who has prior experience with the patient, ideally. I know, Michael, you were talking about how the intake needs to talk with HomeCare HomeBase. One of the reasons for that is you need to...understand if it's a rock or a sock as an example, right? So if it's a rock, then we'll try to send ideally the same nurse back into the patient's home. It's going to prioritize that. And then caregiver preferences and patient preferences. If someone says, I only want to, I want to work with, I want a male caregiver, I want a male clinician, I don't want a female clinician, or I'm allergic to dogs, I don't want people with dogs. These are things that are considered.preferences that the agent would take into account. I just want to be super clear, all of these things are the things that we've fine-tuned with you. If you think clinicians should not have a say on which regions they go to, that becomes a hard requirement. If you think they should have lots of control over that, that becomes a heuristic.That's how we fine-tune the model, the brain, in the beginning, as we deploy, and then it learns with every piece of interaction with your office staff and your clinicians.I want to pause it for a second.

**[0:40:02] Colin Highland:** So, do so do clinicians have some kind of effect on the heuristics piece, or is it a devoted just office leaders, or how does that set up?

**[0:40:15] Kunal Sarda:** Yeah, same Colin. So I'm going to show you really quickly what the clinician experience looks like. So as I said right at the top of the call, a thing that a clinician doesn't think is their assistant fails.

**[0:40:22] Colin Highland:** Mhm.

**[0:40:28] Kunal Sarda:** Right. And so a big piece of this is a any technology like this has to be seen as reduction in effort for the office and the clinician, but also something that understands the clinician much more deeply and is able to take those things into account much more deeply than people are able to, quite honestly, scale.Okay, I'm going to show you the clinician side really quickly on what that looks like. Do you have do we have questions on this? Whatever I showed you here that is seems nonsense or doesn't seem to sit sit well with how we're thinking about scheduling today.

**[0:41:06] Colin Highland:** No, I think that's, I think you'll probably get into the time range of things here a little bit on the clinician side.

**[0:41:15] Kunal Sarda:** Yeah. Okay. So let me share my screen again and just show you what the clinician experience looks like to start with Arya, because again, it all starts with building the context graph on like what the clinician cares about, right? It's obviously learning all of the things that have happened already.Inside of HomeCare HomeBase, that has all the visit information, that has all the productivity points, it has all of those basic things, it has their addresses, all of those things. But the way our customers typically start with Arya.Sorry, I'm bouncing 2 devices.Okay, so the first thing that Arya does, and I guess I'll ask you a question first here, are we treating the are we treating the EMR as the HRIS or is there is sort of employment information and new hire information sitting is it sitting in a workday or someplace else? That'd be that'd be one of the things that we should we should chat about.

**[0:42:12] Colin Highland:** Yeah, we have some sits in HomeCare HomeBase, but most of that would be out of work day.

**[0:42:18] Kunal Sarda:** Okay, cool. So you'll see here the very first point of entry for a clinician into Arya is as soon as Arya discovers a new clinician has been onboarded and they hit HomeCare HomeBase. Again, this is configurable team. Like I said at the beginning, everything, including the language that we use, is configurable at an enterprise level. The first thing that Arya does is...

**[0:42:33] Colin Highland:** Mm.

**[0:42:41] Kunal Sarda:** Yeah, and by the way, this is all two-way. A clinician can text back to Arya at any given point in time, and we'll talk about sort of...how this thing learns from every interaction, how this thing takes action, like call outs and stuff that Evan was pointing out, right? Okay, the very first thing it will do is it will ask you for preferences. Now, I'm going to show you that it's going to drop you into a link here, but I also want to tell you these kinds of things are available directly through chat as well. Some of our customers want these things to be super secure. So you'll see here, I don't need to remember any passwords. We have no...app for clinicians. We have a very strict never build an app policy for clinicians because no clinician wants to have yet another app that they need to log into. Okay, so this is the kind of a preferences app. We set up a very basic one here, team. This is a very typical one that you'll ask your PRNs to say, for example, like what days.Do you typically like to work? It's going to ask you a few different questions. Okay, what times do you typically like to work? And then one of the things it's going to ask you, depending on this is configured at a branch level. I'm hopeful we've done this.is going to ask you like, hey, where do you want to, depending on what branches you work with, what areas are you comfortable going in?Okay, now these are things that we can digitize with you based on the terrible, I call them terrible because I think all of us would agree, the printouts that we have at the office, we can ingest those things to start. But any new clinician that's coming on board, you can imagine that they're getting digitized from day zero when they're coming on board with the organization. So some of that is how do you bring on board the ones that we have.

**[0:44:03] Colin Highland:** Yeah.Not.

**[0:44:22] Kunal Sarda:** And some of them is about how you bring them on, how you bring on new clinicians on board.Okay, so this becomes the foundation for a lot of the preferences, the regions that people want to travel to. By the way, these are things that our customers will configure Arya to reach out to and just double check every couple of weeks proactively, but this is also available at any given point in time when I interact with Arya at any given point in time.It's learning on an ongoing basis as well.

**[0:44:50] Colin Highland:** And I definitely see, you know, this is something we'd of course talk about later on, but this has given me a lot of great ideas over some of the issues that arise within a branch with leaders not setting the correct expectations for clinicians, you know, setting it up, especially within the onboarding process, you know, they've got to

**[0:45:06] Evan Kramer:** Yeah.

**[0:45:10] Colin Highland:** a new employee, they're trying to preserve and, you know, say all the right things to. But by that, the expectations are softened, you know, at the beginning, especially in that courting phase when they're recruiting, trying to approach the hiring phase. And so I could see that piece right there, a wonderful point in time for onboarding alongside maybe a clinical manager that's going to be supervising that clinician to guide them.

**[0:45:32] Kunal Sarda:** Yeah.

**[0:45:35] Colin Highland:** OK, these are your locations that you're signing up for. However, we expect you to cover these areas also. And so that'd be a great way to walk through that process instead of having a clinician fill that out. Yeah.

**[0:45:47] Kunal Sarda:** Yeah.Yeah, you're saying a very important thing here, Colin. I think this is related, but important. You'll see the best time to get a clinician onboarded into technology is when they start.it's much more difficult to change ongoing behaviors. So especially with scheduling, we find that there's a flywheel that gets unlocked. Unfortunately, in our industry, the turnover is so high, right? In the case of technology adoption, that's the only place that that.

**[0:46:03] Colin Highland:** Mhm.

**[0:46:18] Kunal Sarda:** That helps, if you may. It's kind of weird, right? Like, like, what's like the what's the 90 day turnover? I'm like the average is what's sitting at like 40 to 50% right in our industry, so hopefully, hopefully it's a lot lower. I hear Compassus is doing really well at that, right? But even if it's like 30%, 20%, then you imagine one in five nurses are turning over.

**[0:46:20] Evan Kramer:** This in advance, yeah.

**[0:46:20] Colin Highland:** Mm.Matt.Mhm.

**[0:46:40] Kunal Sarda:** On an ongoing basis, this becomes the entry point for them, and if the expectations are set correctly, it becomes the entry point for them.

**[0:46:45] Colin Highland:** Mm-hmm.Great, thank you.

**[0:46:49] Evan Kramer:** Can you on the on the territory stuff, like, so it sounds like you're getting their preferences up front on where they would want to work. Like, does you guys as tool define territories for each clinician and use that as a way of matching patients to clinicians?

**[0:46:56] Kunal Sarda:** You.Yes, so we can adopt that in a couple of ways. We adopt the parent-child. Are we mapping these in HomeCare HomeBase today at the branch level, Evan?

**[0:47:07] Evan Kramer:** OK.I mean, Colin, keep me honest, I don't think so. I mean, this is one of those things that's brilliant.

**[0:47:18] Colin Highland:** Not really. I think that there's a function that's so clunky that most branches don't make use of that. Yeah.

**[0:47:25] Evan Kramer:** It's like a, it's a, I think the way we see it play out is, and I'm generalizing here, but it's like this is the kind of stuff that gets written down on the office whiteboard. And then like the more, we definitely find that the more tenured clinicians have a lot more like social influence.

**[0:47:34] Colin Highland:** Mhm.

**[0:47:44] Evan Kramer:** with the schedulers. So if there's places that they prefer to go versus not go, and there's, you know, the referral sources that they like versus not like, like there's, we see a lot of, I don't want to say gamesmanship, but there's definitely, you know, ways to manipulate this system because it's so undefined today.

**[0:47:57] Colin Highland:** Mm.

**[0:48:02] Kunal Sarda:** Yeah.Yeah, so the number one way, again, because Arya is, Arya doesn't need maps. I just want to say this out loud, because it's always optimizing for drive times. It's trying to, it sets maximum drive time boundaries, Evan, for how much someone wants to, someone needs to travel. So if we are, I would imagine a clinician is still, is a clinician getting hired into a branch.I'm sure that that relationship exists on the on, if nothing else, on Workday.Right, so we'll inherit, we'll inherit that.

**[0:48:33] Colin Highland:** Right, yes.

**[0:48:33] Evan Kramer:** Yeah.Mhm.

**[0:48:37] Kunal Sarda:** And that becomes the foundation for deciding which branch. Now, some clinicians, this is very rare. I think at your scale, it's possible that some clinicians are working multiple branches, but that tends to be tends to be fairly not very common.

**[0:48:48] Colin Highland:** Yeah, not very common, but yeah, it does, yeah.

**[0:48:50] Evan Kramer:** Yeah.

**[0:48:52] Kunal Sarda:** Okay, I want to show you a couple more things here, Tim, because this is all really important stuff. So I just talked about how Arya you interact with, it's a two-way agent that the clinician interacts with and is always learning. So I want to show you here, I asked like, by the way, these are things that I just texted it.what's my schedule tomorrow. And you'll see here it's given me a link for what my schedule is tomorrow. One of the things that we've talked about is this route planning, right? How do you reduce the amount of effort that it takes a clinician to plan their route, change their routes, change their schedule on an ongoing basis? So you'll see here if I click on this again, it's going to drop me.In a...Let me close that out.

**[0:49:37] Evan Kramer:** One other quick question while you're doing that, Kunal. So you said no apps ever for the clinician, right? So, but we're still seeing an interface here, right? So this is basically just like they, they, they, they, I don't know, they, they trigger their engagement through text, it sounds like, and then they're given links to a web app.

**[0:49:43] Kunal Sarda:** Yeah.

**[0:49:56] Evan Kramer:** Right, is that?

**[0:49:56] Kunal Sarda:** Short links, short links, right? So it's going to do whatever work you can do inside the inside the text interface and it's going to give you short links to get stuff done and get out if you need to.

**[0:50:06] Evan Kramer:** Okay, so there's no, yeah, so you guys are trying to avoid them having to like download another app, create a login, sign into it, all that kind of stuff. Like this is just kind of removing a friction point, but you're still getting the same type of engagement that you may have otherwise gotten with an app. Is that fair?

**[0:50:22] Kunal Sarda:** Higher, higher, higher engagement, yeah.

**[0:50:25] Evan Kramer:** Yeah, yeah, okay. Yeah.

**[0:50:27] Colin Highland:** Mm.

**[0:50:28] Kunal Sarda:** Okay, so you'll see here that it's given me my schedule for tomorrow. And what Arya's already done, it's already optimized the recommended route for the clinician for the next day. Based on the patients that I'm supposed to see, based on a specific start time, it said, okay, you want to see, there's only one patient in your team, I'm sorry. But if there was multiple patients, you would see.how it's optimizing across those. I can change the times that I want to start. I can, if I had multiple patients as a clinician, I could move them around. And then when I hit save, there's a couple of ways in which we can do this. I can automatically let your patients know what time the clinician is expecting to see them.But there's also a way in which they can directly message them directly from here, letting them know, hey, I'm going to be coming at this time once I've decided what time they're planning on coming. This piece around the clinician route optimization ends up being one of those things that clinicians are just not good at.And so the ability to be able to recommend certain routes, also, of course, learn from the routes that they've taken. So it's not going to magically just change things around. It's going to try and minimize the disruption of the typical times that they've already seen patients if they're going back into the patient's home. But remember I showed you a time that it was recommended.for a visit on the SOC, it was taking into account what their schedule was, what else is already on their schedule, and trying to fit that inside of their existing schedule, which is how it came up with that time that they should be, they should be doing it.

**[0:52:02] Colin Highland:** So the system doesn't go and contact those patients until the clinician says, OK, my day is what it is. Go. Is that is that for us?

**[0:52:14] Kunal Sarda:** Yeah, and Colin, this is this is the place that I start saying it it depends, which is like we can we can configure this to obviously many clinicians may not even respond to this, right? So, that's the reason why you might say we want we want the clinic we want the patient to know when the clinician is coming anyway.

**[0:52:30] Colin Highland:** I bet they would. I think that because it's a pattern in their every clinician's day. And so, you know, this is this is very intriguing. Yeah, yeah.

**[0:52:39] Kunal Sarda:** OK.So again and again, these things will interact identically with your patient as well, just like I showed you, right? So if they interact with them again, the goal here is to sit inside the inside the workflow of your people. Okay, so let's just stick with.

**[0:52:54] Evan Kramer:** From the patient perspective, like you said that they're triggering a text message, right, that goes to the patient saying that I'll be here between X&Y times. Like, is that coming from the clinician's cell phone number or is that coming from some Arya number that's...

**[0:53:04] Kunal Sarda:** Yeah.Yeah, the one that I just clicked share on would be directly from their phone, but if you were to just save it, Arya would send it from the Arya phone number. That's configured for. We find clinicians to want to sometimes just interact directly with, and we can set this up another way as well. Tim, if you want that to go out from Arya, that's perfectly.

**[0:53:25] Evan Kramer:** Mhm.

**[0:53:26] Colin Highland:** Mm.Mhm.

**[0:53:31] Kunal Sarda:** That's configurable as well, but what I just showed you was native to their was native to their phone if they wanted to just tell someone what's happening.

**[0:53:39] Colin Highland:** Okay.

**[0:53:39] Evan Kramer:** Well, I mean, and I'd be curious to hear your lived experience on this too, Kunal, but like our, one of the things we run into, I think text messages are probably better, but especially when we're calling patients from clinician cell phones, like the pickup rate's really low because they don't recognize that number and it doesn't come through as Compassus.So if there were a way to be able to trigger these messages from something that comes through as like a Compassus number, then I think our response rate and engagement rate would probably be quite a lot higher too. But curious to hear what you've experienced with your increment clients.

**[0:54:11] Colin Highland:** Mhm.

**[0:54:13] Kunal Sarda:** Yeah.Yeah, my very simple soapbox on this, the earlier, as I said this before, the earlier in the patient, you want a single pane of glass for the patient and the caregiver, clinician. So what I'm showing you here is because the clinician first hears when they first start from this phone number, this becomes the way they interact.

**[0:54:23] Colin Highland:** Mhm.

**[0:54:27] Evan Kramer:** Thank you.

**[0:54:35] Kunal Sarda:** Similarly, if you're if you're talking to the patients at the time of discharge, that becomes the single pane of glass. Now, I have to talk to I have to talk to Anand about this. If you're using some kind of telephony service like Twilio or something behind the scenes, depending on what you're using, Evan, we can potentially just use the same phone number.and hook into the same phone number as well to make sure there's a standard phone number that's being used behind the scenes. One other lived experience that I wanted to talk about is we're in the uncanny valley here. Like let me just say this, I can't. So let me just show you really quickly things like call outs, right? That's one of the things.

**[0:55:04] Evan Kramer:** Okay.

**[0:55:17] Kunal Sarda:** You asked.So I don't know if I have this configured as a scale right now, but let's see if I do.Okay, here we go, right? So I have 3 visits that were scheduled for Wednesday. This is the way sort of the re-scramble of the schedule can be handled, right? So I can say like, I want to keep these visits. I can't do them. Now it's Wednesday. Again, all of these things work inside of capacity rules.So what Arya is going to try and do, I'll say, I can't work any of these.Whatever, I'm going to say something like that, right? So Arya first going to try and reschedule inside the clinicians, inside the clinicians calendar, but because it's Wednesday, right? So it's going to work on moving things if it can, if it, because it's Monday today, it's going to try and see if I can move it to Tuesday, for example.But if it can't, then it's going to create callouts and it's going to try staffing them again. All of these visits work on this idea of capacity. This is a very core concept inside of Arya. Capacity means what is a time window within which you need a certain amount of work to happen.So for the start of care, we defined this as 24 hours, right? There's a start time from the discharge to when you want it to happen. For any other visit, for a recurring visit, it might be the Medicare window. So you need to do it between the Sunday to Sunday to Saturday. I think I got that right.For other kinds of visits like wound care, you always want, you don't want certain kinds of visits to be moved. So they may only be on Wednesdays, for example. So all of these things as Arya's deciding whom to staff them with, when to staff, is working on this mental model. I have a certain amount of time in which I have flexibility.

**[0:56:56] Colin Highland:** Mhm.No.

**[0:57:10] Kunal Sarda:** And for each clinician, I'm trying to find for that clinician, what's the best time for me to stop it?So this staffing, it goes to the mental model for every eligible clinician for what specific day this will work for them. What's the best day that this will work for them?

**[0:57:28] Evan Kramer:** Is it also considering the patient's availability?

**[0:57:31] Kunal Sarda:** Yes.

**[0:57:33] Evan Kramer:** Okay, how do you get that?

**[0:57:35] Kunal Sarda:** Let me show you, same way I just showed you.I don't know. I want to sleep in the afternoon.I can't type.

**[0:57:59] Colin Highland:** Ohh.

**[0:58:00] Kunal Sarda:** Let's see if that'll work.Okay, that's a preference that's been noted.

**[0:58:19] Colin Highland:** Mm.

**[0:58:23] Evan Kramer:** Is there something up front though that like, like as the patient is coming on to care that it's saying, it's kind of listing out like, like what are your preferred times across the week or are we just, okay.

**[0:58:33] Kunal Sarda:** Yes, very common way. Again, this can be all of this can be how the agent reaches out from your behalf. I'd set this up as when they're getting discharged. It can proactively ask, are there certain preferences that we should know about?

**[0:58:36] Colin Highland:** Okay.Mm.

**[0:58:48] Kunal Sarda:** as we're staffing for you.

**[0:58:50] Colin Highland:** Yeah, and definitely just know that there's certain preferences that we need to motivate patients past. You know, that everyone's going to say, oh, I want visit times between 10 and 1 and that's not feasible, you know, in our business. And so there's ways, yeah, so there's ways for us to create rules, right, that

**[0:59:05] Kunal Sarda:** We'll try our best, right? We'll try our best to do that.

**[0:59:10] Colin Highland:** maybe even allows the agent to push back a little bit or motivate for, okay.

**[0:59:14] Kunal Sarda:** Yes.Yeah, exactly.

**[0:59:16] Evan Kramer:** How do you, how do you, I mean, Colin, it's, I was thinking the exact same thing. Like, how do you nudge the patient towards like the 9 A.m. slot? Or do you have to?

**[0:59:21] Colin Highland:** Mm.There's actually clinicians, I've got a whole list of like gold standards. Yeah, there's so many wonderful ways that clinicians, I mean, we have all these tricks of the trade. That would actually be a really fun thing for us to engage our clinicians with, you know, give us your tricks. What, you know, what do you do to, I mean, there's so many skills out there that

**[0:59:29] Kunal Sarda:** There's.

**[0:59:44] Colin Highland:** high functioning clinicians have developed already and you know how to politely persuade a patient to take. Yeah, right, right. Yeah, yeah.

**[0:59:51] Kunal Sarda:** This is selling. It's selling. It's selling. Yeah, I'll be fresh. I'll be fresh in the morning when I see you.

**[0:59:56] Colin Highland:** Mhm.

**[0:59:58] Kunal Sarda:** Wanna make sure, right? This is this the same way as a clinician's calling out. Hey, these patients need your care. If you don't, if you don't take them now, we may not be able to get them the care that they need, right? It's those are the kinds of things that these that we can that we can configure deeply to make sure we are balancing this well.

**[1:00:00] Colin Highland:** Uh-huh.Matt.Based off of really what the clinician wants, if it goes against really what the clinician wants, it'd be interesting to find ways to, you know, have, because that's where a lot of clinicians fail. They're not good at, some are just way to...flexible, and then it affects them from an efficiency standpoint. And so, you know, finding ways for this tool to give the clinicians more, you know, nurses, you know, just generalizing a little bit here, but nurses struggle sometimes that more than therapists sometimes, just different archetypes.

**[1:00:55] Evan Kramer:** Can I like...

**[1:00:55] Michael Thompson:** I think we'd also have the opportunity to feed. Yeah, I'm thinking about like when this information would become available. And to me, this feels like, you know, as we think about some of our welcome call scripting and we're already interacting with the patient, you know, can we start actually, you know, can we tailor that scripting before even the clinician interacts with them?

**[1:00:57] Evan Kramer:** Oh, go ahead, Michael.

**[1:01:17] Colin Highland:** Right.

**[1:01:19] Michael Thompson:** clinician can sell, but that initial base list of factors and preferences, that's some discrete information that could be passed through to the algorithm from the platform.

**[1:01:21] Colin Highland:** Mhm.Mhm.Mhm.Because that really is.

**[1:01:31] Kunal Sarda:** Well, Michael, like, just to just to tell you, sorry, Colin, didn't mean to interrupt.

**[1:01:35] Colin Highland:** Oh no, oh no, but just what I was going to say was that, you know, a lot of times I've seen plan of cares get poisoned by how flexible the start of care clinician is with maneuvering towards the desires of the patient or caregiver. And so every subsequent clinician from the add-on disciplines to then the case manager, they're all now having to

**[1:01:49] Kunal Sarda:** Okay.

**[1:01:56] Colin Highland:** to function in that pattern that was developed at that initial interaction with that patient, which you want to, you know, be pliable and you want to, you know, this is customer service we're providing, but there's also a business and efficiencies and other clinicians that need to be able to have visits be scheduled at the times that work best for them. And so, yeah, there's right up front is really where it's a long story. Yeah, that right up front is where

**[1:02:13] Kunal Sarda:** Yeah.

**[1:02:20] Colin Highland:** the patterns get developed.

**[1:02:23] Kunal Sarda:** Yeah, the rabbit hole of this is so deep team and I always say a lot of context problems are created upstream. So like this thing that we're capturing the nurse preferences. So we have this thing called a talent agent that does the screening for nurses to get them scheduled for an interview with a recruiter. You should technically capture that information like.The amount of information that doesn't flow in from the recruiter into the branch is astounding.

**[1:02:47] Colin Highland:** Mhm, mhm.

**[1:02:47] Evan Kramer:** Sheth.

**[1:02:48] Kunal Sarda:** Similarly, the amount of information that doesn't flow in from intake, like if they're talking to the patient into the branch, into the nurse's hands for scheduling, like the softer stuff is probably A lot. That's what we're referring to. So that's why I said the earlier, this is why we call it a common context problem. And that's why we have a very wide.

**[1:03:00] Colin Highland:** Mhm.Mhm.

**[1:03:07] Kunal Sarda:** product which is like you need to touch intake and you need to touch talent to be able to capture as much of that up front to improve the experience without having to capture more of this information downstream.

**[1:03:17] Colin Highland:** Interesting, yeah, good.

**[1:03:20] Kunal Sarda:** So yeah, but my soapbox aside, I think that's exactly the answer, which is capture this information at the point of entry for the patient. Create the communication layer that they have available to be able to communicate with them. And by the way, these things are smart enough. They're not going to go off the wall and say, I'm telling you about the weather.

**[1:03:28] Colin Highland:** Mhm.Mm-hmm.

**[1:03:42] Kunal Sarda:** They're going to be very narrowly programmed to answer specific kinds of questions, and if they can, they'll escalate it to, they'll say escalate it to the office. One of the things I haven't done for you today, team, is these agents are multimodal. They work over text and voice.

**[1:03:57] Evan Kramer:** I was going to ask about that. Okay.

**[1:03:59] Kunal Sarda:** So you can call into, a clinician can call into this, and I will, if you would like, I will actually configure a voice agent for you that you can play around with yourself, and I can send that to you afterwards. So things like needing to call out, things like needing to change their schedules, have questions about XYZ, a patient has questions about XYZ,my clinician didn't show up or something else happened. These voice agents, we call this front desk. These voice agents manage inbound calls. Now I think someone said this, and by the way, these voice agents do outbound calls. So if you're trying to fail someone, I don't know, do we have that enabled here, Anand? I'm trying to see.

**[1:04:40] Anand:** Sorry, which one?

**[1:04:41] Kunal Sarda:** Did we have outbound calls enabled and texting enabled for specific patients? Okay, I don't see it here. We'll show you.

**[1:04:48] Anand:** No, I don't think we configured it.

**[1:04:51] Kunal Sarda:** We can show you a demo of that next time also, Tim. So here you'll see Arya's making recommendations, but the list of eligible caregivers is probably much longer. If I had enabled that for you, the office tab would just be able to click a button and Arya can call all your clinicians who are eligible and ask them if they can work with the patient, negotiate over the phone or negotiate over the text.They don't have to go through the round robin of doing that manually. And then similarly, they can, clinicians can call in if they have any kinds of questions, just like they were texting back and forth. But we find our lived experience, since you asked me this question, Evan, our lived experience, older clinicians.prefer calling, younger clinicians prefer texting, and so you need to have both of those things available for different strokes for different folks. One of the preferences that we'll capture is what times, how many times can we harass you in a day if we need to call you. So we're not texting people incessantly, for example, because again,The nurse, the nurse is the the nurse is the product here, so we can't we can't annoy them. So having control over what times they want to be called, is it okay to call them, is it okay to text them, or things that will capture as part of the preference during onboarding as well.

**[1:06:03] Evan Kramer:** Yeah.

**[1:06:05] Colin Highland:** So the fact that a clinician could call into Arya, technically, could someone place a call, ask what their schedule is for the next day, listen into it, and then say, move Mrs. Jones to 9:00, and then Mr. Smith to

**[1:06:15] Kunal Sarda:** Yeah.

**[1:06:24] Colin Highland:** That 1:00, um, they're able to do that, and that would in that interaction, that would does that.

**[1:06:28] Kunal Sarda:** Yep.Yep, it won't happen. The way it works is because that introduces a lag, it will capture it and then complete it afterwards, call in asynchronously. Yeah. And then confirm.

**[1:06:40] Paige Huffman:** What about for, I'm sorry, what about for our patients that are Spanish speaking or do not speak English? Will it send text in a different language or it will?

**[1:06:51] Kunal Sarda:** and voice and voice as well, Paige. I'll send you a demo of it. You can play around with it. I think you'll find that. It's, we're in the uncanny valley now.

**[1:06:59] Colin Highland:** Right. Now, have you found, as far as patient engagement goes, have you found, I know a lot of clinicians use techniques of getting that patient or caregiver to answer the phone in that time that they need to get that schedule confirmation.

**[1:06:59] Evan Kramer:** Yeah.

**[1:06:59] Paige Huffman:** Thompson.

**[1:07:17] Colin Highland:** A lot of clinicians will call, not leave a message, then send a text if no one answers, and then call back, leave a message if after a certain period of time, can the agents leave a voicemail too for that? Okay.

**[1:07:18] Evan Kramer:** Mm.

**[1:07:32] Kunal Sarda:** Yeah, yeah, it was very because we we work in the talent and recruiting space. This this concept of needing to do it multiple times, leaving a leaving a message, then calling back to make sure people pick up is is very common when you're dealing with a high friction.

**[1:07:39] Colin Highland:** Mhm.Right. Because normally telemarketers, if it is a telemarketer, it doesn't call twice. And so a lot of times patients and caregivers, if they get a phone call from the same number within a short period of time, not to overly annoy them, but that's just what clinicians do to get that phone to pick up. And so interesting.

**[1:07:55] Kunal Sarda:** Yeah.Yeah.How many times you call back, how many times you call back and text is configurable, and how quickly you call back and text. Since we're always talking about sort of our lived experience and just sort of what we've seen, team, one of the things that I will push you on pretty early is how much inside the patient experience do you want AI to be?

**[1:08:14] Colin Highland:** Mhm.

**[1:08:24] Kunal Sarda:** Like, do you want to start there?And the reason I say that is we have all the tools, but what we typically find with providers is, and I think at your scale, probably you're willing to, and given your DNA, you're probably willing to lean in some more. What we typically find is providers are very, they always, I always say the provider-patient relationship is, no pun intended, a little fragile.is always considered a little fragile, so people feel a little bit more on the back foot to introduce technology. They want to introduce technology to the patient last, as opposed to the first or one of the first times. So I think that's one of the conversations we'll have around what's the right level of introduction.

**[1:09:05] Evan Kramer:** I think we'll be pretty forward leaning on that. Yeah, I'm obviously very forward leaning on it, but I think our clinical operating counterparts may reel us in just a little bit. But, you know, as you've seen on the rest of our, you know, AI deployments, Kunal, I think there's been a big embrace of AI across the...

**[1:09:05] Kunal Sarda:** And.

**[1:09:17] Colin Highland:** Right.

**[1:09:25] Evan Kramer:** organization so far. So I think that's exciting. I think that's a really, really interesting capability you guys have there. I have two more questions just kind of related to this here. So the first one is that when I think about the business case for this, one of the biggest opportunities I think we have.is taking the patient coordination or scheduling burden off of the clinician, right? And, you know, I'm sure you've seen this in other clients, but at Compassus, our schedulers aren't really schedulers, they're like more admin people. The people who are picking up the phone and actually scheduling are the clinicians, and that's a...bottom of the license, like frankly, waste of time, you know, when you consider what we're paying them for licensed work. Like, and it takes probably 30 to 60 minutes a day, right? So I guess my first question is, what's been your observation with other deployments on how much of that time you guys are able to reduce?with these kinds of capabilities that we're talking about here.

**[1:10:29] Kunal Sarda:** Yeah, the two, there's two parts to answers to this. One is how well can this get transferred from the clinician to something else, whether that be people, because the admin staff are a significantly lower cost resource that we're just talking about money. And the second piece is how much more efficiently.

**[1:10:39] Evan Kramer:** It.

**[1:10:49] Kunal Sarda:** Can someone do this versus doing it versus doing it themselves? So, the biggest, the biggest bold case for this team is that this gets taken off the off the clinician's hands.But that's the biggest, that's the biggest bull case for this. They have, they have to be kept in the loop, so this system can completely transfer over, like the, the, you can think of this as the clinician in the loop as opposed to the clinician who does the, like, it's a flipping of the script.

**[1:11:04] Evan Kramer:** Yeah, I agree.Yeah.

**[1:11:19] Colin Highland:** Mhm.

**[1:11:19] Evan Kramer:** Yeah. Well, and that's what I'm asking though, is that it's like in the world that we're in today, the clinician is picking up the phone, calling every single one of those patients, probably not getting a hold of them every single time, right? Like there's a lot of inefficiency there and it takes time for them to actually have that conversation. So if I'm understanding your product correctly,

**[1:11:20] Kunal Sarda:** If you may.No.

**[1:11:39] Evan Kramer:** it looks to me like they're just like they're coordinating everything in the app or the web app, right? And they're triggering a bunch of automated patient engagements, right? Whether it be text message or voice AI, all that work is being done autonomously by the app, right? And the coordination is happening and the app is helping them to optimize their route.So I got to imagine that 60 minutes of like manual voice time for the clinician has got it compressed down into 10 or 15 minutes of app coordination time. Is that a, am I thinking about that the right way?

**[1:12:13] Kunal Sarda:** It should be, it should be close to 0, with the exception coming back to the clinician.

**[1:12:18] Colin Highland:** Mhm.

**[1:12:19] Kunal Sarda:** at the end of the day, right? It becomes an exception handling.Situation, right?

**[1:12:24] Evan Kramer:** So the clinician's not actually triggering every one of these messages, then like the app is recognizing where it wants to put the patient in the schedule and it's just going out and doing it.

**[1:12:32] Kunal Sarda:** Show that, so we can, so there's two, again, there's two workflows, show it to the clinician, have them confirm it and then do it, or do it and then tell the clinician, here's what I've done, right?

**[1:12:39] Colin Highland:** Mhm.And I, and I bet, and I bet that if there was a trigger, hey, you know, your schedule as of 5 P.m., you know, if you gave clinicians some type of timeline, you know, for automation to occur, if you haven't had a chance to go and manipulate things, but I think that this is a great way for clinicians to...

**[1:13:01] Colin Highland:** I mean, there's some change management here where I could see over time as clinicians started to trust the system more and more, take a look at that calendar for the next day and saying, okay, looks good. I think that over time, you've probably learned that in some of your other deployments that a lot ofchanges in the times probably at the beginning, but then over time, clinician noticed, okay, yep, I trust it. That looks good. You know, nothing new that I've got to add or no extra info that I know about that patient or caregiver that would, you know, stop that time from being a reasonable time for them, right?

**[1:13:38] Kunal Sarda:** Yeah, I mean, it's one of those things I was having a really interesting conversation with a large provider the other day, not as a bit of a segue.There's people who trust these things implicitly, and there's people who learn to trust these things, and I was talking to actually Evan, who was the head of innovation at a very large provider, and he was like, "We've just partnered with him, and he, he, I was, I asked him like..."Why are you so forward leaning? He drives the Tesla self-driving car. And he's on full, he's on FSD, full self-drive. I'm like, I haven't been, I'm not comfortable with it. Why did you get comfortable with it? And his answer was like, when the car does something that's different from me,I wonder, hmm, what else does it know that I didn't think about?As opposed to assuming that is wrong.

**[1:14:28] Kunal Sarda:** So there's going to be two camps of people here, right? One campus that will be very trusting and they'll say, okay, this looks like, okay, it's probably figured something out. It's recommending a different route than I typically would have taken. Looks good. The other one will be who will want to give it feedback, make it better, and then trust it.

**[1:14:31] Colin Highland:** Mmh.

**[1:14:38] Evan Kramer:** Play.

**[1:14:48] Kunal Sarda:** trusted more over time. Those are the two camps of clinicians that you'll find as you as you deploy this.

**[1:14:54] Evan Kramer:** Yeah.

**[1:14:56] Colin Highland:** It just added on top of what evidence said too about the forward leading into automation. And this, I think that this is just a piece of the engagement layer that clinicians have to have with their patients on an ongoing basis. And it's the less important piece, the scheduling phone calls. This opens the door for clinicians. They're not losing that relationship with these patients. There's still going to be reasons for these clinicians to nowcall one of their patients because they needed to follow up on something versus, you know, having to be burdened with these, you know, low-level tasks that we're talking about. And so I think that, you know, I think that clinicians will start to appreciate the fact that now they have that time to maybe follow up with that call that AI couldn't do for them, right?

**[1:15:41] Kunal Sarda:** So I think we're sort of leaning into, Evan, please go ahead.

**[1:15:46] Evan Kramer:** Sorry, I've got so many questions. Okay, so the second question that I have for you was, it sounds like there is a lot, or the system is capable of rejigging the schedule as many times as it needs to to ensure that it's optimal throughout the day, right?I guess that one of the factors in there is continuity of care. And so like if you don't care about continuity of care, then you've got a lot more opportunity to optimize, but a lot of patients care about that, right? So I'm curious to hear how you guys have thought about that. And I'm sure it's a constraint in your model, but like,How much have you been able to relax that constraint? And yeah, curious to hear more about the experience.

**[1:16:36] Kunal Sarda:** Yeah, so again, the continuity of care, and I'm assuming you're referring to like making sure the same clinician is going into the patient's home as an example, right? This is what we call a heuristic. It's one of the most important factors in how RA decides whom to staff with, right? So if you work with the, making sure the same clinician is going into the patient's home is one of the really important

**[1:16:43] Evan Kramer:** Yeah.

**[1:16:58] Kunal Sarda:** factor, probably it's one of the highest rated factors, I would say, across all of these other things as a deciding whether you should staff with someone else or not. So making choices, Evan, is going to force, and again, we fine tune this to make sure we force things. And I want to show you, I prefer answering these kinds of questions with a little bit of...with a little bit of data, if you may. So inside of the system team, as we talk about, maybe if I could kill two birds with one stone, how do you know if these things are working? So the way these things work is we store, we lean on data, right? And we say all of the decisions that Arya is taking.How frequently are your, maybe your office, your schedulers, or your clinicians rejecting the decisions that Arya is taking?

**[1:17:48] Evan Kramer:** Mhm.

**[1:17:49] Kunal Sarda:** And what are the reasons that is rejecting? Why they're rejecting it? So these are the things that Arya learns from. And this becomes a really important sort of change management tool as well to understand like what's happening and what are the reasons that people are not are rejecting the things that Arya is doing so we can.Fine-tune the model, right? So, Evan, we end up we end up treating this from day zero when this thing is launched. We're seeing who's accepting it, who's rejecting it, what's happening, and we use the data to say what's missing in the fine-tuning that we need to that we need to improve from here also caregiver engagement, like we'll know.Like, who's filling out preferences? What are the preferences that they filled out? How much do we know about the clinician? Is that that do we know enough about the clinician to be able to do a good job at meeting their preferences? When we're reaching, when Arya is reaching out to clinicians, how often are they engaging?are the ones that are new to Arya, are they engaging more frequently than the ones that are, like where are the gaps? And one of the things that we look at is we call these things agent health. So let's say, Evan, we said, hey, we want to make continuity of care a very, very important thing. Like we want to, we don't want to make it a heuristic, we want to make it a hard requirement.No, no, no clinician can go into the patient's home if they haven't worked with them before. So one of the things we measure, and there's no data behind this here, but one of the things we measure is like for on average for a patient, how many times are we even able to find a clinician based on the rules and heuristics you've defined? So we'll actually use this data to say how well do we need to fine-tune this further given.given what's actually happening on the field? Or are we restricting things so much that we need to dial back certain things or dial up certain things? So because all of this is digitized, all of the decision making is digitized, all of the reaction and feedback is digitized, this ends up being a really, really important piece of sort of our...deployment cycle in the early days to understand especially how we pilot and this is going to bring me to my last point on sort of change management as you talk about clinicians and the office staff on how to how to launch this well but we lean on data pretty heavily to make not hide behind anything and to see like what are the decisions that are being made how we how we train the engine.And is it making good decisions or not?

**[1:20:15] Colin Highland:** Mhm.And then the reverse of that is the lens that this platform can give the branch leaders into patterns, maybe at the clinician level, right? But then also within their branch, you know, that the goal of affecting capacity is for these branches to be able to grow and to

**[1:20:18] Kunal Sarda:** Ah.Yeah.

**[1:20:37] Colin Highland:** to make the best decisions to facilitate that growth, you know, and find those patterns that our leaders don't have the time or the resources or, you know, the ability to visualize, you know, the decisions that need to be made.

**[1:20:51] Kunal Sarda:** Yeah, absolutely. I mean, one of the things that in my in my demo I haven't showed you to team is I've said once a patient is...Once you have a patient, how do you staff them? The first thing that Michael said was there's a staffing decision, the capacity decision that probably has to happen upstream from that. So knowing like, should we, do we have the capacity to see a patient? How often do we actually have the capacity to see a patient?All of this gets moved upstream.

**[1:21:19] Evan Kramer:** Mm-hmm.

**[1:21:20] Kunal Sarda:** and can get and should get moved upstream. Now, we have customers that will say, like, don't care, like, we have to find a way to serve a patient. I don't care about capacity, get them in the system and we'll figure out how to staff them. At your scale, you're probably saying, like, we have to make sure.We can staff them before we accept them.

**[1:21:37] Colin Highland:** Mmh.

**[1:21:37] Michael Thompson:** There's different, there's different scenarios at different branches. That's what scale has created, is that we've got some branches. I mean, we got branches all across the spectrum here. So we've got a plan for it all. There's not a one size, there's not a one size branch here in these markets.

**[1:21:40] Kunal Sarda:** Yep.

**[1:21:41] Colin Highland:** Right.

**[1:21:41] Evan Kramer:** Yeah.

**[1:21:43] Colin Highland:** Mhm.No.And sometimes the branches need to be pushed to accepting more than what they feel they can, just because by de facto, discharges get delayed and referrals fall through. And so, you know, having a partner that's able to, a system that's able to help these branches make those decisions.

**[1:21:54] Evan Kramer:** What?

**[1:22:13] Colin Highland:** because you can't brutally just accept the exact number of spaces you have available because things always fall out.

**[1:22:17] Kunal Sarda:** Yeah.So as an example, pre-admission, the capacity window can be set to a week from the referral date to say, do we have anyone in the next week to be able to take care of them? As you get closer to the discharge date, the capacity window can be brought down to a week to say, okay, now it's time to really staff with the right person, the person that we need to staff with.

**[1:22:38] Colin Highland:** And.And in my experience, a lot of the spinning of wheels happens with the welcome calls and the contact to the patients and caregivers being delayed. You know, a lot of times, you know, the resources, sometimes those are the last things that are done and they start at 4:00 in the afternoon by a scheduler and thenYou learn so much stuff. You know, there's so many times where patients and caregivers, even though they're being discharged on Friday, they say absolutely no to a weekend visit. And so that visit all of a sudden is a Monday. And so, you know, having a way to automate and garner that information as soon as possible, because in real time, if you knew that, if that welcome call had happened atone in the afternoon instead of at 4, you could have accepted two more referrals possibly, right, to get to that. And so I think that the, you know, the systems tool of being able to automate those welcome calls can give that branch and the system that information so much, because the goal is 24 hours to 48 hours, but

**[1:23:25] Kunal Sarda:** Yeah.

**[1:23:40] Colin Highland:** The patients and caregivers often drive that timeline too, and we're able to write orders that reflect those requirements and still, you know, get them scuttled out, of course.

**[1:23:51] Kunal Sarda:** Yeah, I mean, we'll be fine. Please go ahead.

**[1:23:51] Michael Thompson:** Can I?Yeah, yeah, can I, if it's okay, just looking at 30 minutes left, there's a couple of just core things that I'm rattling around my head that I'd like to just like to understand further.Can you, can we, can you please help me understand what is the scheduler's interaction with this tool now? And what is a day in the life of a clinician's interactions with this tool? So core questions like, I think we saw, you know, I'll just do a little bit of setup just so you guys can try to hit all the pieces thatI'm trying to figure out is we get a new referral that comes through and I know we were like on the demo we were going we wanted to see those three different scenarios there of rescheduling of recurring visit.We get a new referral that comes through. The scheduler gets the percentages there. Is some like who is controlling that assignment there? Is that automation or is that human? Is there a human touch there? And then from there, I think I understand the escalation part of the of the scheduler's piece there, but.

**[1:24:57] Kunal Sarda:** Yeah, great.

**[1:25:03] Michael Thompson:** Is there a stop before it hits the schedule, before it hits the clinician schedule that somebody is interacting with that piece? Right here. Yep.

**[1:25:12] Kunal Sarda:** No, so think of this, Michael, as I've said, we've set up this demo as a thing that creates the office staff as the hard stuff.Right to say you have to approve.

**[1:25:23] Michael Thompson:** Oh, okay. This is if we wanted a hard stop for everyone. Got it.

**[1:25:27] Kunal Sarda:** Yes, sir. But the agent will inform the office staff. So the way you want to think about this is, is the office staff in the loop versus the office staff approving things, right? So the way this agent works in this case, it's created a hard stop to say, hey, I need you to approve.

**[1:25:34] Michael Thompson:** Yep.

**[1:25:45] Kunal Sarda:** the things that we've done here. Again, this is how we typically will say like build trust with the office this way. But once this is up and running, the office staff is being told I am staffing a new case that is coming right now. Okay, and I have staffed this new case or I have not been able to staff it. I need you to get eyes on this.So this is what we call like the critical items. I don't, I haven't been able, I've reached out. No clinicians seem to be available. I need you to need you to figure out if anyone can take this case. So the, so the scheduler's experience is in the loop.

**[1:26:07] Michael Thompson:** Cut.Okay.

**[1:26:25] Kunal Sarda:** while things are happening. And like I said, we have integrations into Microsoft Teams, integrations into e-mail to inform the scheduler on what's happening. And then if something needs to be escalated to them, because there's some staffing that is unable to happen, then that gets escalated and they would come in here and take action and see what.What is done?

**[1:26:46] Michael Thompson:** Let's flip it to the clinician then, that makes sense. So now we've got this pass through, it's finding coverage for it. And then we saw the one which was it auto, you know, it'll auto assign to the full timers where it'll provide the opportunities for the part timers. Is it?

**[1:26:53] Kunal Sarda:** Yeah.

**[1:27:06] Michael Thompson:** Um...Is there any interaction with the clinician before it drops on their schedule? So right now it's passed through on the scheduler. Now it's getting to the clinician. What is that, you know, so I think one of the core questions that I have coming in as I'm looking at these is that Colin is so well stated is thatyou know, clinicians want to make sure they feel like they've got control and autonomy over their schedule, right? That's one of the core reasons why they come to home health, even though that they need to be productive and they need to meet baseline expectations, they still want a semblance of control. So help me understand what the future of

**[1:27:35] Kunal Sarda:** Yep.

**[1:27:47] Michael Thompson:** that is using this platform.

**[1:27:49] Kunal Sarda:** The exact reverse of what, it's not even future, it's present, Michael. It's the reverse of this, which is Arya determines who are the eligible clinicians. It will reach out to clinicians and say, hey, can I staff you with this patient? Here's what I recommend. I can staff you with this patient. The clinician says yes.

**[1:28:07] Michael Thompson:** Amazing. Okay. Okay.

**[1:28:09] Kunal Sarda:** So, it's not it's not different, right?

**[1:28:09] Colin Highland:** So that helps, so that that solves for like the coverage. Oops, sorry.

**[1:28:13] Kunal Sarda:** dot com.

**[1:28:15] Colin Highland:** So that solves for like the coverage needs of the branch, right? Thursday afternoon, they need 3 evals covered certain territories. Is there a way to configure that coordination to occur?

**[1:28:29] Kunal Sarda:** Yeah, autonomously as the thing comes in, Arya can autonomously reach out. And again, like this is just a different setup that I can show you the next time we chat on.

**[1:28:31] Colin Highland:** The.And it can reach out like in a batched way, so you know, all PTs get contacted. Okay.

**[1:28:39] Kunal Sarda:** Yeah, yeah, yeah.Yes, yes. And batch, not just batch, but not blast everyone and their uncle, the best ones whose calendar seems to fit the most first, then into the second batch if we found no one, then dip into, then dip into the.

**[1:28:43] Michael Thompson:** Right.

**[1:28:49] Colin Highland:** I bet.And that's a benefit that you have AI agents that are the foundation of this is that there's logic and learning that is interesting.

**[1:29:01] Kunal Sarda:** Yeah, let me just show you, Anand. I wonder if I should do this now. I don't want to expose another customer, guys. I can't show you, but like the setup is very simple. It shows you, it will run through the eligible clinicians in the order in which they're the best fit. Reach out to them, see if they're willing to take the...Patient, if they're not, is going to work down the list to see if someone else can, which which becomes more clinician-driven again.

**[1:29:24] Colin Highland:** Mhm.So in the office, it would almost feel like, you know, whether it's a scheduler or a clinical manager, it would almost feel like they had another teammate on the team. They would speak to Arya, explain what needed to have happen, and then that agent logic would take that in and take that new set of context.

**[1:29:45] Kunal Sarda:** Yeah, let me just, um, I don't want this, I want to make this real for you.Because it probably sounds like I'm talking paperware right now. So let me just...Let me just show you really quickly.Okay, Anand, are you still there?Is there an account on prod I can show with the...The.

**[1:30:16] Anand:** Yeah, I'm going to see if I can enable this in Arya QA, but I think we might not have check it.

**[1:30:24] Evan Kramer:** Well, he's bringing that up, Kunal. How many, how far in advance do you guys enable scheduling to take place? Because right now we do it just the day of, right, or the night before, which is inherently suboptimal. But it seems like with this type of coordination between patient and clinician, et cetera,You theoretically could go multiple days, maybe even a couple of weeks, and through it.

**[1:30:47] Kunal Sarda:** Yeah, that should never, it should never be, never, never be one. Like the only thing it should be a day at a time is the start of care because you're like, okay, the patient is getting discharged. We need to, or lock, right? A sock or a rock probably needs to get happen fast, but then anything else, the frequencies are set in the future within the authorization window. Anything that's within the authorization window should be getting scheduled in advance.

**[1:30:55] Evan Kramer:** Yeah.And then one other question, like, you know, we're talking about kind of matching the right clinician to the right patient here. Like, I've actually deployed a tool like this, you know, a number of years ago while I was still in consulting to another company, was not healthcare, but very similar type of, you know, you know, optimization type of work.And one thing that we found was is that in order to optimize at the aggregate level, there were sometimes outliers that came out where it's like maybe one person ends up with a sub-optimal recommendation for them so that we can optimize for everyone else over here. And so I guess I'm...You like usually that person's not very happy about that. So curious like how you guys deal with that in your system.

**[1:31:57] Kunal Sarda:** Yeah, so this is a question, I'll be honest, like we're still working through, Evan, which is how many people do you want to disrupt?to minimize the total level of disruption.I think what you're referring to logistically is like if a new case comes in and...If there's one clinician who can take it and it's going to ruin their day, then we need to move around three other calendars to make sure it doesn't ruin their day, as an example.

**[1:32:27] Colin Highland:** Mhm.

**[1:32:28] Evan Kramer:** Well, it's either one, right? It's like you could avoid ruining their day and impact a number of other people's schedules, which may not be the worst decision to make. Or it's like you got an appointment that came or a patient that came in that is like pretty far outside of this person's quote un quote territory.So they're going to be upset if they are forced to go out there and see that patient, but they're the only one, right? And like, in order to avoid blowing up everyone else's schedule, like we just need them to go do this visit, right? Like, how do you, like, and the reason why I'm asking this is because in today's world, like you've got a human scheduler who has a relationship with these nurses that calls them up and says, hey, look, man,I gotta call it a favor. Like, I need you to go out and do this here. In the future, if we're using this tool and it's all happening autonomously, like this is one of those situations where the clinician could look at this and be like, man, this tool is crazy. Like, like why is it giving me this ridiculous, what is it recommendation, right? So, so how do you, how do you handle those types of situations?

**[1:33:25] Kunal Sarda:** There's no way I'm doing this.Yeah, I can tell you two specific ways in which we've helped our customers handle those situations, which is create a give and take in the system.

**[1:33:41] Evan Kramer:** What do you mean?

**[1:33:41] Kunal Sarda:** As an example, hey, I'm making you go all the way here.If you do this, I can lighten something else for you.In the future, like one, like one really dumb thing that we've done is like...

**[1:33:52] Evan Kramer:** Okay.

**[1:33:56] Kunal Sarda:** Lump up the productivity points on that.

**[1:33:59] Colin Highland:** Mhm.

**[1:34:00] Kunal Sarda:** On the thing you're going to do.

**[1:34:00] Evan Kramer:** I mean.

**[1:34:00] Colin Highland:** Yeah, and so, yeah, incentives, add some incentives to that, yep.

**[1:34:02] Evan Kramer:** Luke.

**[1:34:03] Kunal Sarda:** Second, add incentives, add incentives, we we offer it, we we have a bonus thing that's in the agent. Hey, I can offer a bonus for this because I know you're going to be driving way out of the way.

**[1:34:08] Colin Highland:** Mm-hmm.Mhm.

**[1:34:13] Evan Kramer:** Yeah, and does that work? Have you seen that work?

**[1:34:17] Kunal Sarda:** Yes.

**[1:34:18] Evan Kramer:** Okay, I figured it would, but...

**[1:34:20] Colin Highland:** Yeah, branches use that, yeah, that's always the last ditch effort, but...

**[1:34:22] Kunal Sarda:** But then the the other question you ask is, like, how frequently will people game it? Is the next question you ask, like, so everything's everything's is a give or take.

**[1:34:28] Evan Kramer:** Yeah, it is.

**[1:34:33] Colin Highland:** So, could, so could Arya order DoorDash to that clinician's home for later on, if they're if they're working past?

**[1:34:40] Kunal Sarda:** I mean, yeah, we, we, this is, I mean, I know that we're laughing about it, but we literally have a negotiation scale, um, built into the agent, so to be able to offer incentives.

**[1:34:40] Evan Kramer:** Yeah.

**[1:34:50] Colin Highland:** I mean, car washes go a long way for home health clinicians.

**[1:34:56] Kunal Sarda:** Anand, are you still updating that? I want to show a couple more things here, team, as Anand's pulling this so we don't run out of time here. We didn't really talk about...

**[1:34:56] Evan Kramer:** Not a bad idea, man.

**[1:34:58] Colin Highland:** I've used it before. Oh yeah.

**[1:35:08] Kunal Sarda:** Change management. I don't want to leave this conversation without that piece. I think, as you, I've said this to Evan many times, like, I'm really proud of the technology that we've built here. I think is really, really disruptive in a good way, but none of that works without a few sort of core building blocks that we like, we like to partner with deeply.If you would allow it right, so the first thing here is...I can tell you that the leadership on this team standing in front of clinicians telling everyone how amazing this anything is since sliced bread is only going to go so far.And the number one thing we can do is to build internal advocates.And so where you start really matters.

**[1:35:51] Evan Kramer:** Luke.

**[1:35:54] Kunal Sarda:** And which branches you start with really matter, branches where you have a forward leaning director, ED, who has good relationships with their clinicians matters. And then the way we typically do this is a couple of things, like we'll actually build, like having internal case studies.really matters. Now this is something that's more sort of office driven, but the number one thing that's going to make clinicians believe they should do this is other clinicians.So building a real, like, and unlike documentation, right, and Evan, we've talked about this many times, unlike documentation, like easy to deploy, these things are like seen as massively disruptive. So making sure like there's lots of assets around how these things work, ask questions, have lots of testimonials.like create a real internal selling mechanism to be able to go to your clinicians about why this matters. The second thing, which you're hopefully not going to laugh at, but in the early days, because you just mentioned bonuses, one of the things that we have to do frequently to get the flywheel turning.is actually deploy rewards.to get clinicians to start pulling and turning the flywheel. Hey, every time you've scheduled a visit through this, for the 1st 90 days, we create rewards programs at the office level for clinicians to take the leap, do the work, ask questions.

**[1:37:16] Evan Kramer:** Yeah.

**[1:37:22] Kunal Sarda:** And, like, all of these things matter tremendously, so...I think this is the, like when we talk about our lived experience, this is probably one of the most important pieces of our lived experience, which is where you start matters.I mean, getting the communication right from us to the clinicians, but secondly, creating advocates that can that can really we can put on a pedestal.really matters and third incentives like what's in it for me like the like the their lives being better as a future promise like having some other short-term promises that help them take the leap and go through the micro friction early days.Is really, really important.

**[1:38:06] Evan Kramer:** We've done, yeah, I mean, couldn't agree more, you know, like we've done all three of those things in our various deployments. And I think that's one of the powers of Michael and his team is, you know, like we work like hand in glove with the clinical operating leadership. Andwe identify the most forward-thinking programs that we could deploy this stuff into. Like, the nice thing is, is that like, whereas maybe a year and a half ago, we were kind of trying to force this on people, like AI in general on people, now we've got a couple of RVPs out there that are like asking, hey, when's the next thing coming? Like, can I be the tester for it, right? So.

**[1:38:34] Anand:** It.

**[1:38:47] Evan Kramer:** I think there's a lot of internal demand for this kind of stuff. And you know, the rewards that you mentioned, I've seen that work really well here too. So I think you guys think about it exactly the same way that we think about it. And I think we're really well set up from a maturity standpoint to be able to tackle something like scheduling now that we've kind of knocked out some of these first couple of.of initiatives here.

**[1:39:10] Kunal Sarda:** Love it. Love it. I want to show you really quickly sort of what this looks like since you were asked this question. You see the same interface, Michael, Colin, but what it's done is reached out. Instead of just, instead of saying who are the right people, Arya has reached out out of eligible clinicians.Called and texted them.see who wants to take it and then escalate it back to the office. As an example, saying, do you want to approve this? This is another flavor. It can automate that and just say, just have the office out of the loop if he wants to.

**[1:39:42] Colin Highland:** Mhm.And how do you keep the leadership in the loop there? Because I think that certainly there could be clinicians calling into the office. And if a manager or scheduler didn't have a concept of what the clinician was calling about, I could see that would be awkward. So is that something that there's also like notifications in some way that

**[1:39:49] Kunal Sarda:** Okay.

**[1:40:09] Colin Highland:** Grant understands what's being, yeah, yeah.

**[1:40:09] Kunal Sarda:** Yeah, any kind of staffing decision that Arya is making, it will escalate back through a notification, whether that be Teams or whatnot, but this becomes your central view for like all of, and I don't see here. Hey, you'd asked about, you'd asked about continuity of care.

**[1:40:16] Colin Highland:** Okay.Mhm.

**[1:40:28] Kunal Sarda:** Evan, so I wanted to show you this really quickly here as well. This seems like this is set up for, it's recommending, these are not great matches, but it's recommending someone who can cover more of the visits on an ongoing basis than someone else, making sure continue of care, like even from the initial staffing decision, is happening in a way that drives for continue of care.

**[1:40:41] Colin Highland:** Yeah.

**[1:40:47] Kunal Sarda:** Just, this is just data out in the wild at the moment.

**[1:40:50] Colin Highland:** OK, so that would be recognizing, hey, this is the clinician that's tied to that territory who would, you know, very likely be assigned subsequent visits. Let's see if we can get this OK.

**[1:41:00] Kunal Sarda:** Yes.Yes.

**[1:41:02] Michael Thompson:** I think that was a question I had too, and just kind of two of these is, one, do you see these kind of 0% sticky situations more on sock rocks, or do you see it more on disrupted schedules once they're already live? Like where?

**[1:41:05] Colin Highland:** Mhm.

**[1:41:22] Michael Thompson:** Where are they? I'm just because I'm trying to think. I think that'll hit the follow-up question that I have.

**[1:41:27] Kunal Sarda:** Yeah, let me, Michael, can I give you an OBS answer?

**[1:41:30] Michael Thompson:** Please.

**[1:41:32] Kunal Sarda:** The no BS answer is...Giving the clinician too much control.I think, I think finding the middle ground, like we find organizations that are saying, hey, the clinician gets to decide the two cities they go in.

**[1:41:46] Michael Thompson:** Yeah.Yeah, I was looking at that too being saying like, well.

**[1:41:54] Kunal Sarda:** Yeah.

**[1:41:58] Michael Thompson:** You know.I don't, you know, I'll go to part of Irvine, but I'm not going to go to all of it kind of things, right? I mean, this is some of that control, that preference, like how much do you just lean in there versus, you know, it's an interesting conversation. But let's say that we,

**[1:42:05] Colin Highland:** Mhm.Right.Right.

**[1:42:18] Michael Thompson:** What I'm trying to figure out is...We could give, we could pass the information with a projected start of care date and essentially bring it back to the people except declining and saying, yes, this is a place that we typically schedule, but when we're looking to schedule this, we're probably going to be in a 0% situation. Is this a patient that we should even be saying yes to to begin with? Like, but if...If that's not the issue, if it's more often that, yes, we get them on, that's okay, but then disruptions start happening during their episode, and in their episode it's actually creating a lot of fallout that's really hard to manage because of it, then it's not a start of care problem, it's a...It's a down the road, you know, physician control. Why are you disrupting this? We're not looking far enough ahead. Like, you know, and all of a sudden we're creating situations for us three weeks into the episode. Like, I just don't know if you've got any insights and like, where is the bottleneck?

**[1:43:03] Kunal Sarda:** care. It's like a recurring care problem.Yeah.Yeah, the, I mean, all of them, all of them might go. I mean, the bottleneck is we don't have enough nurses.

**[1:43:22] Michael Thompson:** Yeah, I know, yeah.I mean, from a technology perspective, like, do you, from the people who use it, do they find more challenge with needing the incentives up front? Or is it just ongoing and just kind of part of the cycle, no matter what the schedule issue that comes up is stating?

**[1:43:28] Kunal Sarda:** Right.Yeah.Usually up front because there's fewer RNs than LVNs and LPNs. RNs tend to be more full-time, fewer in staff, there's more flexibility on the LVN, LPN pool. So we find that to be less of an issue, relatively speaking, between starting versus recurring. I see Paige shaking her head. Paige, you haven't said much. I'm curious about what you.What do you think about that?

**[1:44:11] Paige Huffman:** I'm just soaking it all in. That makes sense. It does, from my limited experience in the home health offices, it makes perfect sense.

**[1:44:20] Kunal Sarda:** Yeah, the other thing that can happen there, Michael, is like, obviously for knowing whether we have enough staffing, we need to have know the frequency and stuff, but we can make certain assumptions about the frequency and start servicing up recurring staffing. Do we have the recurring staff for this or not? Not just start a care.

**[1:44:35] Colin Highland:** And that's, that was actually a segue into what I was wondering is, you know, there's a lot of protocols that, you know, there's orthopedic surgeons that have known protocols, there's wound orders that are that are part of the referral information that comes through. So trying to project out based off of, you know,Daily wounds, you know that, yeah, yeah.

**[1:44:53] Kunal Sarda:** You have enough data, you have enough data to know what might be the needed frequency for needed frequency of care for a patient before the start of care has happened. So technically we should be able to project out not just do we have the RN for the initial visit, but also do we have the ongoing staff through the same.

**[1:44:58] Colin Highland:** Mhm.

**[1:45:12] Michael Thompson:** Yeah, how far do you project out?

**[1:45:15] Kunal Sarda:** Well, our customers will, like you said, like no one's doing it one day out. Michael, I can tell you that. Most typically, customers are doing it one month out up to the authorization window, obviously.

**[1:45:26] Michael Thompson:** Good. Okay, that's what I'm wondering. I'm thinking about, because I mean, this is the other side of the saying yes, saying no decision. Like how, we haven't spent a lot of time there and I know we're running short here, but maybe if you could give us a high level about how your capacity planning model work.Like, uh, and, and uh, yeah, how does that work?Yeah, I'll stop there.

**[1:45:53] Kunal Sarda:** Yeah, so super high level, I described this idea of capacity in Arya, which means it starts with all of the patients that need care for every piece of care that they need, Arya defines a capacity window within which that care has to be delivered.As an example, the starter care has a capacity window of 24 hours. A recurring visit that needs to happen inside of the Medicare window will have a window of seven days. A wound care specific visit types that must happen on a specific day for any reason will have capacity windows that are tied to a specific day of the week.

**[1:46:30] Colin Highland:** So that would fall into like insurance, known insurance authorization constraints, right? And what does the system do when there's frequency that extends beyond like the off with an insurance? Okay.

**[1:46:36] Kunal Sarda:** Yep.It's not going to schedule. It's not going to schedule beyond the auth. It's going to escalate. It's going to escalate.

**[1:46:46] Colin Highland:** Is there a way for the office to, is there a way for the office to visualize that though? Because you still have to account for the, yeah.

**[1:46:51] Kunal Sarda:** We, we actually...We ask, we escalate at the moment through a notification that we're about to run into a authorization window, at which point it can't be scheduled anymore, so we give, we give heads up on, we give heads up on the staff to get additional authorization to continue scheduling for the page.

**[1:46:59] Colin Highland:** No.Mhm.Okay. And there's a lot of scenarios where we know the auth is going to be approved. It's just part of the workflow and the process working with that insurance company. Do you have a solution for like blocking just so that that that anticipated visit that we anticipate to be there is still being part of the equation of

**[1:47:26] Kunal Sarda:** Yes, let me just show you that instead of telling you that. Let me see if I can.

**[1:47:33] Anand:** Also, Kunal, I think it's better if we come back on the capacity stuff, the UI that you were asking. We don't have, we don't have good data, so.

**[1:47:42] Kunal Sarda:** Yeah, no worries. That's okay.That's OK. Here, I'll just show you this really quickly, Tim. It doesn't have to be exactly right, but here you here you'll see there is another state called put in review. It creates a hold column, so instead of instead of finalizing or it can put in a hold that time.

**[1:47:48] Colin Highland:** Okay.Okay.Okay, so it knows that it's potentially happening, so it's not being forgotten. It's still part of the logic, but okay.

**[1:48:04] Kunal Sarda:** Yeah.Yes.Yes, yeah.

**[1:48:13] Evan Kramer:** Another question from my side. I know we only have 8 minutes left and kind of a totally different area, but I want to, I think I know the answer to this. I just want to make sure and ask it anyway. So when we think about like all the work that is going to get done autonomously or through some, you know,human engagement with you guys' tool versus actions that may still need to be triggered in HomeCare HomeBase. I want to make sure I'm really, really clear on that. So does you guys' tool make it essentially so that nothing has to happen in HomeCare HomeBase and we're just running back in at the end of the day? Or are there still pieces of the HomeCare HomeBase workflow that need to be managed?by the clinician or scheduler.

**[1:48:58] Anand:** I think that will depend on the workflow that we build and based on your requirements as well. Preferably, we would like to not even have to manage between HomeCare HomeBase and Arya and you be able to do everything in Arya. But again, it will depend on the workflow that you have that you actually do in HomeCare HomeBase that you want to keep it there.There is also change management involved, right? Like there are certain things that PHI and stuff that we don't want to touch. So it will depend exactly on that as much as possible. We would like to keep everything in Arya so that nobody has to use HomeCare HomeBase for day-to-day tasks.

**[1:49:33] Kunal Sarda:** So just tactically speaking, Evan, so let's say there's a clinician assignment, right? So let's give a very simple example of a clinician says, I'll work with this patient. Arya will plot the start of care and assign it to the clinician.In HomeCare HomeBase, as an example, those are the kind of things you're asking, right?

**[1:49:49] Evan Kramer:** Yeah.

**[1:49:50] Colin Highland:** OK, and so that means that this, that means that scheduling workflow isn't left to open-ended. The system completes that workflow, so we don't have stuff piling up.

**[1:49:57] Kunal Sarda:** Yeah, our job guys, our job team isn't to tell you what, like our job is to do the work that a scheduler does, which involves having a near real-time view of what's happening on HomeCare HomeBase. Just to be super clear, HomeCare HomeBase will be kept as your source of truth.

**[1:49:58] Anand:** Oh yeah.

**[1:50:03] Colin Highland:** Mm.

**[1:50:17] Kunal Sarda:** That's like because that is your source of truth. That's what you build from. So all of the visits, ultimately when Arya decides, well, should this clinician work with someone, it's actually listening back to HomeCare HomeBase and saying what are they actually scheduled for already. And any changes it's making is writing back to HomeCare HomeBase.As well.

**[1:50:38] Evan Kramer:** Yeah, OK.

**[1:50:39] Anand:** Yeah, I mean, I also want to say one more thing. Like if you're using another system like the tracker system or the product that you were talking about, if that is a source of truth for some other information, and if Workday is a source of truth for caregiver information, then that will stay the source of truth for them. It's not just HomeCare HomeBase, it's just a connector for us. So we will work with you, figure out with what the source of truth is, and then we will set that as the source of truth.

**[1:51:03] Kunal Sarda:** Yep, so like clinicians, for example, their demographics and their employment status and their brand status, you'd say like, HomeCare HomeBase sucks. Maybe we don't have half the information, so we will make work day, for example, the source of truth for that. But schedules, visits that are being scheduled, authorization windows.

**[1:51:03] Evan Kramer:** Okay.Yeah.Yeah.

**[1:51:22] Kunal Sarda:** frequencies, those things are probably all definitely sitting in HomeCare HomeBase as an example.

**[1:51:27] Evan Kramer:** Yeah.

**[1:51:28] Colin Highland:** And with the buildup of all these rules, is there a way to see the roles that have been created through the interaction with Arya so that if we need to backtrack and clean up maybe some of the interactions that maybe, you know, maybe a clinician kept saying no to certain things and Arya learned, you know, nos versus yeses andyou know, is there a way for us? Maybe that's a question for, I mean, we're probably going to spend, you know, another point in time together at some point soon, but...

**[1:51:58] Kunal Sarda:** Yeah, we're built the answer to that is Colin, we're building the visualization so you can see what the brain is. If we like, if we talk again, we'll show you exactly how we're planning on visualizing the entire logic so you can see exactly how that's working. Not just not at a like a decision by decision level, but like what's the brain, how is it making decisions? We've actually just figured out how to visualize that.

**[1:52:04] Colin Highland:** Mhm.The.Mhm.Okay, that's great. I could see how that would be important, especially to folks that aren't technologically inclined. They're probably going to want to see it so they can at least visualize a little bit. Okay.

**[1:52:31] Kunal Sarda:** Yeah, you also saw, I don't know if you saw on the screen that I showed you, every decision it's making, it's showing you why I think this person is the best fit.

**[1:52:38] Colin Highland:** Mhm.

**[1:52:39] Kunal Sarda:** saying, okay, it's overtime, mass continuity of care, closest to the patients, matches their preferences. That's it's going to give you kind of the mental model on every decision, but what you're describing is sort of what's the organizational.model and to be able to change that. Yeah.

**[1:52:53] Anand:** Context here.

**[1:52:56] Kunal Sarda:** That's the piece that we're building at the moment, the visualization of it.

**[1:53:00] Colin Highland:** Mhm.

**[1:53:00] Evan Kramer:** Yeah, we haven't talked about integration requirements yet. I'm assuming that if you guys have worked with HomeCare HomeBase, you know, the RPA is the only option.

**[1:53:10] Kunal Sarda:** Yeah, we've talked, we've talked with Colin, like I think their marketplace and their API are supposedly coming in 2027, so we're all waiting with bated breath on that one Citrix-based browser automation having this, the usual, the usual trio.

**[1:53:18] Evan Kramer:** Yeah.What's the minimum refresh cadence that you guys need from the log shipping?

**[1:53:29] Kunal Sarda:** I was just, I was just arguing with Anand about this. Go ahead on.

**[1:53:37] Anand:** I think, see, with Citrix, it's fun exercise figuring out the SLAs. It all depend on what rules that you've set within like the authentication system itself. And one of the things that we've noticed with multiple customers is that you actually there is there is a hub.If you use like Okta and stuff like that, it actually disconnects you every 20, 30 minutes. That means that you would have to log in every time into the Citrix system itself that we have to use. If that is not the case, then we can definitely like figure out and come to an SLA of like 15 to 20 minutes for the reads.And, and for the writes again, like depending upon the amount of data and how many logins that we have to provision for the write backs, if they that will basically define it, but we're trying that that will be around like 15 minutes as well. We are trying to like make it depends like one thing that I've noticed with HomeCare HomeBase implementations is like with each customer.The way some things are set up is slightly different. So we'll work, we have, once we get like sand, if you're getting like sandbox access or not, then we'll be able to figure out if it is matching what we have right now. If it is matching what we have right now, we should be able to get that in like 10, 15 minutes. So that's usually the cadence that we're following right now.

**[1:54:53] Kunal Sarda:** Also, Evan, we'll do load testing on the sandbox to tell you that we can meet those SLAs at the scale, depending on what the scale of the reads and the writes are. That's a part of our deployment process.

**[1:54:53] Evan Kramer:** Okay.

**[1:55:01] Anand:** Yeah.

**[1:55:07] Evan Kramer:** Yeah.Okay.I know where it's at.

**[1:55:12] Kunal Sarda:** Tim, I know we're at time. This is my magical superpower. I don't know if you've noticed, we're going to end this right on time. So we really appreciate, we appreciate you all. Thank you for all the good questions and excited to chat some more if it makes sense.

**[1:55:16] Anand:** Stop.

**[1:55:19] Colin Highland:** Bye.For sure. No, I think that I can speak for all of us. I think that we probably would benefit from a little bit more time together at some point. And so I think that we'll meet and, you know, find, I'm sure that there's some stairway thoughts that will come to our minds as we're putting our thoughts together. And so we'd love to have an opportunity toCome back with some follow-ups.

**[1:55:51] Evan Kramer:** And that's another virtual call, right, Colin? Like, hey, Kunal, I'm sure you saw the e-mail. Like, we're looking, unfortunately, we wanted to go faster, but the week of October 19th is when we're looking at doing the on-sites. So the good thing is that gives us a little bit more time to get a little bit deeper with you all virtually before we select who's going to come on for the on-sites.

**[1:55:54] Colin Highland:** Yeah, yep.

**[1:56:13] Evan Kramer:** So yeah, well, Colin can help. Colin Paige can help coordinate our next touch point here.

**[1:56:18] Colin Highland:** Yeah.

**[1:56:22] Kunal Sarda:** We're here, standing by.

**[1:56:24] Colin Highland:** OK, great.

**[1:56:25] Evan Kramer:** Cool. Thank you all. Really appreciate it. Thanks.

**[1:56:26] Michael Thompson:** Thank you, everyone. Thanks, guys. Really enjoyed it. Take care.

**[1:56:26] Kunal Sarda:** Thank you. Thank you. Bye.

**[1:56:27] Colin Highland:** Thanks, everybody. Bye.

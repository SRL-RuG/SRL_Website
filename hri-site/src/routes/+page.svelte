<script>
  import { base } from '$app/paths'

  // Detailed course information

  let course = {
    title: 'Social Robotics Lab',
    faculty: 'Science and Engineering',
    year: '2023-2024',
    code: 'WMAI027-05',
    levels: 'Master',
    credits: 5,
    period: 'Semester 2a (2024-02-05 - 2024-04-14)',
    language: 'English',
    coordinator: 'P.A. Vogt PhD',
    lecturer: 'P.A. Vogt PhD',
    lecturerWebsite: 'https://www.ai.rug.nl/paulvogt/',
    literature: [
      {
        title: 'Human Robot Interaction (freely available online)',
        author:
          'Christoph Bartneck, Tony Belpaeme, Friederike Eyssel, Takayuki Kanda, Merel Keijsers, and Selma Sabanovic',
        isbn: '9781108735407',
        type: '',
        price: '',
      },
    ],
    remarks:
      'This course unit has a capacity limit. Intended limit of 60 participants.',
    prerequisites:
      'Recommended: Cognitive Robotics. Prior knowledge of Python is useful, but not required.',
    learningOutcomes: [
      'Explain the core principles underlying human-robot interaction for social robots.',
      'Combine theories about human communication, cognition, and behaviour to develop natural interactions between social robots and humans.',
      'Apply methods of user-centred design and AI to develop HRI for social robots.',
      'Design, carry out, and analyse experiments in HRI.',
    ],
    description:
      'Social robots are entering our society at an increasing speed, providing support in education, healthcare, hospitality, and other domains. This course focuses on designing AI for robots that can communicate socially with humans in an effective and efficient manner, including verbal and non-verbal gestural communication.',
    teachingMethod:
      'Lecture, Practical. Students work individually and in groups on a research project.',
    assessment:
      'Report, Presentation, Assignment. Final grade based on assignments (30%), research report (50%), and video presentation (20%) with a minimum of 5.5.',
  }
  let professor = {
    name: 'Dr. P.A. Vogt',
    title: 'Assistant Professor',
    department: 'Artificial Intelligence',
    researchInterests: [
      'Human-Robot Interaction',
      'Social Robotics',
      'Cognitive Systems',
    ],
    email: 'p.a.vogt@rug.nl',
    office: 'BB 410',
    website: 'https://www.ai.rug.nl/paulvogt/',
    imageUrl: 'Pics/2018-tiu-340-vogt.webp', // Replace with actual image path
  }

  let isOpen = false

  function toggleAccordion() {
    isOpen = !isOpen
  }
</script>

<!-- Hero Section -->
<div class="hero bg-hero-gradient">
  <div class="hero-content text-center">
    <div class="max-w-md">
      <h1 class="text-5xl font-bold text-primary-content ">{course.title}</h1>
      <p class="py-6 text-primary-content">{course.description}</p>
    </div>
  </div>
</div>
<!-- Course Details -->

<section id="course-details" class="container mx-auto p-8">
  <div
    class=" w-full py-4 grid md:grid-cols-3 gap-2 sm:grid-cols-1
    justify-items-center">
    <!-- Course Information Card -->
    <div class="flex-grow card bg-base ">
      <h3 class="text-2xl font-bold text-center m-3">Social Robotics</h3>

      <div class="accordion-summary ">
        The development of social robots is advancing fast, but their ability to
        interact with humans –especially with a-typical populations– is still
        limited in scope, form and effectiveness. For example, automatic speech
        recognition (ASR) is often flawed, except for most adult speech when
        processed through the cloud, which slows down interactions and thus
        effectiveness and acceptability of the communication. Also, non-verbal
        interaction (e.g., through hand gestures), considered essential for
        effective communication with humans, is hard to achieve in a meaningful
        manner. Another challenge is to design the human-robot interaction such
        that the robot can understand human behaviour and can understand whether
        the human understands the robot, and that the robot responds in an
        appropriate manner.
      </div>

      {#if isOpen}
        <div class="accordion-content">
          <p>
            Furthermore, the robot’s environment is changing continuously either
            due to its own behaviour, that of the human or through some other
            external source. The robot should be able to adapt to this dynamic
            environment. Finally, especially to facilitate long-term
            interaction, the robot should learn to interact with humans in a
            personalised manner for which it should be able to develop some form
            of common ground. The Social Robotics Lab aims to address these
            issues, taking an interdisciplinary approach combining theories from
            communication studies, (psycho)linguistics, psychology, social
            sciences and other related fields to develop and apply AI techniques
            in the design, development and evaluation of social robots in
            several domains. These include education, health care and elderly
            care.
          </p>
        </div>
      {/if}

      <div
        class="button-container"
        style="text-align: center; {isOpen ? 'margin-top: 1rem;' : ''}">
        <button on:click={toggleAccordion} class="btn btn-accent m-2">
          {isOpen ? 'Read less' : 'Read more'}
        </button>
      </div>

    </div>

    <div class="divider divider-horizontal md:visible sm:invisible " />

    <!-- Coordinator Information Card -->
    <div class="flex-grow card bg-base ">
      <h3 class="text-2xl font-bold text-center m-3">Coordinator</h3>

      <figure>
        <div class="avatar">
          <div class="w-40 rounded-full">
            <img
              src={professor.imageUrl}
              alt="Profile image of {professor.name}" />
          </div>
        </div>

      </figure>
      <div class="card-body">
        <h2 class="card-title">{professor.name}</h2>
        <p>{professor.title}, {professor.department}</p>
        <div>
          <strong>Research Interests:</strong>
          <ul>
            {#each professor.researchInterests as interest}
              <li>{interest}</li>
            {/each}
          </ul>
        </div>
        <div>
          <strong>Contact:</strong>
          <p>Email: {professor.email}</p>
          <p>
            Website:
            <a class="text-primary" href={professor.website}>
              {professor.website}
            </a>
          </p>
          <p>Office: {professor.office}</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Course Information Section -->
<section class="bg-base-300 p-8">
  <!-- Course Information Section -->
  <section class="bg-base-300 p-8">
    <div class="card">
      <h2 class="text-3xl font-bold text-center">Lab Information</h2>
    </div>
  </section>
  <div class="container mx-auto grid md:grid-cols-2 gap-2 sm:grid-cols-1 ">

    <!-- Overall Structure of the Course -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">
        <h2 class="text-2xl font-bold">Robots</h2>
        <div class="card card-side bg-base-100 shadow-xl">
          <figure>
            <img
              src="https://www.cmihva.nl/wp-content/uploads/2021/10/A_MINI_2-600x600.jpg"
              alt="AlpahaMini" />
          </figure>
          <div class="card-body">
            <h2 class="card-title">Alpha Mini</h2>
            <p>
              Equipped with 14 high-performance servos, Alpha Mini can achieve a
              wide range of flexible movements inlcuding walking, dancing and
              push-up. Rich sensor array and accurate algorithms also help Alpha
              Mini realize dynamic balance control and obstacle avoidance.
            </p>
            <div class="card-actions justify-end">
              <a
                href="https://www.ubtrobot.com/consumer/humanoidRobots/alphaSeries/AlphaMini">
                <button class="btn btn-accent">Learn more</button>
              </a>
            </div>
          </div>
        </div>
        <div class="card card-side bg-base-100 shadow-xl">
          <figure>
            <img
              src="https://luxai.com/wp-content/uploads/website-refactor/qt-robots/Qtrobot-arm-up-happy.png"
              alt="QTRobot" />
          </figure>
          <div class="card-body">
            <h2 class="card-title">QT robot</h2>
            <p>
              QTrobot is an expressive social robot designed to support a
              variety of use-cases including education of children with autism
              and other special needs education and human-robot interaction
              research and teaching.
            </p>
            <a
              href="https://luxai.com/humanoid-social-robot-for-research-and-teaching/">
              <div class="card-actions justify-end">
                <button class="btn btn-accent">Learn more</button>

              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Lectures and Practical Sessions -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">

        <h2 class="text-2xl font-bold">Opportunities</h2>

        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">Bachelor thesis projects</h2>
            <p>
              The bachelor projects are designed to engage students in the
              development and exploration of social robotics within various
              contexts, including elderly care, interaction enhancements using
              ChatGPT, co-speech gesturing, and empathetic behavior in robots.
              These projects aim to improve human-robot interaction through
              programming and testing with real robots like Alpha Mini and QT,
              incorporating activities such as literature review, solution
              design, and evaluation with human participants.
            </p>
            <a
              href="https://www.ai.rug.nl/paulvogt/wp-content/uploads/2024/01/bachelor_projects.pdf">
              <div class="card-actions justify-end">
                <button class="btn btn-accent">Find out more</button>
              </div>
            </a>
          </div>
        </div>
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">Master thesis projects</h2>
            <p>
              The master projects in social robotics focus on developing and
              researching how social robots can effectively and meaningfully
              communicate with humans across different groups and application
              domains, such as education for children and healthcare for the
              elderly.
            </p>
            <a
              href="https://www.ai.rug.nl/paulvogt/wp-content/uploads/2024/03/Master_projects_PV.pdf">
              <div class="card-actions justify-end">
                <button class="btn btn-accent">Find out more</button>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Literature Overview -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body card-content">
        <h2 class="text-2xl font-bold">Research topics</h2>
        <ul>
          <li>Grounding communication in social robots</li>
          <li>
            Child-robot interaction, robot tutors
            <ul>
              <li>
                <a class="text-primary" href="http://www.l2tor.eu/">L2TOR</a>
                project
              </li>
            </ul>
          </li>
          <li>
            Ethnographic research on language socialisation
            <ul>
              <li>
                <a class="text-primary" href="http://www.l2tor.eu/">
                  CASA MILA
                </a>
                project
              </li>
              <li>
                <a
                  class="text-primary"
                  href="https://cordis.europa.eu/result/rcn/223816_en.html">
                  HADZA
                </a>
                communication
              </li>
            </ul>
          </li>
          <li>
            Computational modelling of language acquisition
            <ul>
              <li>
                <a
                  class="text-primary"
                  href="https://ilk.uvt.nl/~pvogt/one/COSLI.html">
                  COSLI
                </a>
                project
              </li>
            </ul>
          </li>
          <li>Gesture use in language acquisition</li>
          <li>Maternal responsiveness and social media use</li>
          <li>Experimental semiotics</li>
          <li>Co-constructions in interaction</li>
          <li>Word learning experiments</li>
          <li>Child-computer interaction</li>
          <li>Social symbol grounding</li>
          <li>Language evolution</li>
          <li>Language grounding in robots</li>
          <li>Concept formation</li>
        </ul>
        <div class="card-actions justify-center">
          <a
            href="https://www.ai.rug.nl/paulvogt/publications/"
            class="btn bg-accent text-accent-content">
            Publications
          </a>
        </div>
      </div>
    </div>

    <!-- Courses Section -->
    <div class="card bg-base-100 shadow-xl">
      <div class="card-body">
        <h2 class="text-2xl font-bold">Courses</h2>
        <!-- <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">Social Robotics</h2>
            <p>
              Social robots are entering our society at an increasing speed,
              providing support in education, healthcare, hospitality and other
              domains. Now, what makes a robot a social robot? And, how can we
              design, implement and experiment with social robots?
            </p>
            <a href="https://ocasys.rug.nl/current/catalog/course/WBAI062-05">
              <div class="card-actions justify-end">
                <button class="btn btn-accent">Ocasys</button>
              </div>
            </a>
          </div>
        </div> -->
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">Social Robotics Practical</h2>
            <p>
              In this practical course students gain knowledge and understanding
              of the main principles underlying social robotics, and learn to
              design, implement and experiment with the basics of social robots.
            </p>
            <a href="https://ocasys.rug.nl/current/catalog/course/WBAI062-05">
              <div class="card-actions justify-end">
                <button class="btn btn-accent">Ocasys</button>
              </div>
            </a>
          </div>
        </div>
        <div class="card bg-base-100 shadow-xl">
          <div class="card-body">
            <h2 class="card-title">Human-Robot Interaction Social Robots</h2>
            <p>
              Social robots are entering our society at an increasing speed,
              providing support in education, healthcare, hospitality and other
              domains. To facilitate the development of adequate robots, the
              field of Human-Robot Interaction (HRI) investigates how social
              robots best interact with humans in order to enhance the quality
              of support these robots can give.
            </p>
            <a href="https://ocasys.rug.nl/current/catalog/course/WMAI027-05">
              <div class="card-actions justify-end">
                <button class="btn btn-accent">Ocasys</button>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Schedule Section -->
<!-- <section id="contact" class="bg-base p-8 text-center">
  <h2 class="text-3xl font-bold">Schedule</h2>
  <div class="overflow-x-auto">
    <table class="table w-full">
      <thead>
        <tr>
          <th>Week</th>
          <th>Date</th>
          <th>Lecture</th>
          <th>Date</th>
          <th>Practical</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1</th>
          <td>6 Feb</td>
          <td>Introduction to social robots</td>
          <td>7 Feb</td>
          <td>Intro robots</td>
        </tr>
        <tr class="hover">
          <th>2</th>
          <td>13 Feb</td>
          <td>Verbal and non-verbal interaction</td>
          <td>14 Feb</td>
          <td>Verbal interaction</td>
        </tr>
        <tr>
          <th>3</th>
          <td>20 Feb</td>
          <td>Design of HRI, research methods</td>
          <td>21 Feb</td>
          <td>Non-verbal interaction</td>
        </tr>
        <tr class="hover">
          <th>4</th>
          <td>27 Feb</td>
          <td>Robot companions in elderly care; Long-term interaction</td>
          <td>28 Feb</td>
          <td>Project start</td>
        </tr>
        <tr>
          <th>5</th>
          <td>5 Mar</td>
          <td>Social robots in elderly care (guest lecture Sanja Balalic)</td>
          <td>6 Mar</td>
          <td>Project work</td>
        </tr>
        <tr class="hover">
          <th>6</th>
          <td>12 Mar</td>
          <td>Common ground</td>
          <td>13 Mar</td>
          <td>Project work</td>
        </tr>
        <tr>
          <th>7</th>
          <td>19 Mar</td>
          <td>Personalisation (guest lecture Fokie Cnossen) and empathy</td>
          <td>20 Mar</td>
          <td>Project work</td>
        </tr>
        <tr class="hover">
          <th>8</th>
          <td>26 Mar</td>
          <td>Ethics and Robots in society</td>
          <td>27 Mar</td>
          <td>Presentations</td>
        </tr>
      </tbody>
    </table>
  </div>

</section>  -->

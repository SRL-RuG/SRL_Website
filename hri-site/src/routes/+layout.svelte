<script lang="ts">
  import '../app.css'
  import ScrollToTop from '$lib/components/ScrollToTop.svelte'
  import { base } from '$app/paths'
</script>

<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<ScrollToTop />
<div class="navbar bg-base-100 sticky top-0 z-50">
  <div class="navbar-start">
    <div class="dropdown">
      <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h8m-8 6h16" />
        </svg>
      </div>
      <ul
        tabindex="0"
        class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100
        rounded-box w-52">
        <li>
          <a href="{base}/">Home</a>
        </li>
        <li>
          <a href="{base}/literature">Course Literature</a>
        </li>
        <li>
          <a href="{base}/guides">Manuals</a>
        </li>
        <li>
          <a href="{base}/examples">Code Examples</a>
        </li>
      </ul>
    </div>
    <a href="{base}/" class="btn btn-ghost text-xl">SocialRoboticsLab</a>
  </div>
  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal px-1">
      <li>
        <a href="{base}/">Home</a>
      </li>
      <li>
        <a href="{base}/literature">Course Literature</a>
      </li>
      <li>
        <a href="{base}/guides">Manuals</a>
      </li>

      <li>
        <a href="{base}/examples">Code AlphaMini</a>
      </li>
    </ul>
  </div>
  <div class="navbar-end">
    <a href="https://github.com/SRL-RuG" class=" btn bg-accent text-accent-content">Github</a>
  </div>
</div>

<slot />

<footer class="footer footer-center p-10 bg-base-200 text-base-content rounded">
  <!-- First row of links -->
  <div>
    <nav class="grid grid-flow-col gap-4">
      <a
        href="https://ocasys.rug.nl/current/catalog/course/WMAI027-05"
        class="link link-hover">
        Ocasys
      </a>
      <a
        href="https://rooster.rug.nl/#/en/current/schedule/course-WMAI027-05/timeRange=all"
        class="link link-hover">
        Rooster
      </a>
      <a href="https://www.rug.nl/staff/p.a.vogt/" class="link link-hover">
        Coordinator
      </a>
    </nav>
  </div>
  <!-- Second row of links -->
  <div>
    <nav class="grid grid-flow-col gap-4">
      <a
        href="https://brightspace.rug.nl/d2l/home/273084"
        class="link link-hover">
        Brightspace: Human-Robot Interaction Social Robots
      </a>
      <a
        href="https://brightspace.rug.nl/d2l/home/271846"
        class="link link-hover">
        Brightspace: Social Robotics Practical
      </a>
    </nav>
  </div>

  <aside>
    <p>
      Website designed by
      <a
        href="https://www.linkedin.com/in/vlad-iftime/"
        class="link link-hover">
        Vlad Iftime
      </a>
    </p>
  </aside>
</footer>

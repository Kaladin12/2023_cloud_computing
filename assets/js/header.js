
class Header extends HTMLElement {
    constructor() {
      super();
      
    }
  
    connectedCallback() {
      this.innerHTML = `
      <head>
      
    
      <!-- Google Fonts -->
      <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
    
      <!-- Vendor CSS Files -->
      <link href="../vendor/aos/aos.css" rel="stylesheet">
      <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <link href="../vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
      <link href="../vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
      <link href="../vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
      <link href="../vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

      <link href="../css/style.css" rel="stylesheet">
    </head>
        <i class="bi bi-list mobile-nav-toggle d-xl-none"></i>

        <!-- ======= Header ======= -->
        <header id="header">
            <div class="d-flex flex-column">

            <div class="profile">
                <img src='../assets/img/profile-img.jpg' alt="fef" class="img-fluid rounded-circle" id="profile" onerror="this.onerror=null;this.src='assets/img/profile-img.jpg';" >
                <h1 class="text-light"><a href="index.html">Elian Cruz</a></h1>
                <div class="social-links mt-3 text-center">
                <a href="https://github.com/Kaladin12" target="_blank" class="github"><i class="bx bxl-github"></i></a>
                <a href="https://www.linkedin.com/in/elian-cruz-1430a61a4/" target="_blank" class="linkedin"><i class="bx bxl-linkedin"></i></a>
                </div>
            </div>

            <nav id="navbar" class="nav-menu navbar">
                <ul>
                <li><a href="../index.html#portfolio" class="nav-link scrollto"><i class="bx bx-book-content"></i> <span>My Work</span></a></li>
                <li><a href="../index.html#contact" class="nav-link scrollto"><i class="bx bx-envelope"></i> <span>Contact</span></a></li>
                </ul>
            </nav><!-- .nav-menu -->
            </div>
        </header><!-- End Header -->
      
        <script src="../vendor/purecounter/purecounter_vanilla.js"></script>
        <script src="../vendor/aos/aos.js"></script>
        <script src="../vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
        <script src="../vendor/glightbox/js/glightbox.min.js"></script>
        <script src="../vendor/isotope-layout/isotope.pkgd.min.js"></script>
        <script src="../vendor/swiper/swiper-bundle.min.js"></script>
        <script src="../vendor/typed.js/typed.min.js"></script>
        <script src="../vendor/waypoints/noframework.waypoints.js"></script>
        <script
        type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.1.0/mdb.min.js"
      ></script>
        `;
    }

    static get observedAttributes(){
        return ["image_src"]
    }

    attributeChangedCallback(name, old, newV){
        console.log( this.getAttribute("image_src"))
        this.querySelector("img.img-fluid.rounded-circle").src = this.getAttribute("image_src")
    }
  }
  
  customElements.define('header-component', Header);
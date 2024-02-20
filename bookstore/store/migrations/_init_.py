body {
	font-family: 'Open Sans', sans-serif;
	margin: 0px;
	padding: 0px;
	font-color: #fff;
}

/* General link styles*/
a {
    color: #D8562B;
}
a:hover {
    color: #1CBC69;
    text-decoration: none;
}

/* Nav bar styles */
.navbar, .navbar-inner{
	filter: alpha(opacity=90);
	-moz-opacity: 0.9;
	-khtml-opacity: 0.9;
	opacity: 0.9;
    color: #e6e6e6;
}
#navbar .navbar-nav li a {
    color: #D8562B;
}
.navbar-header .navbar-brand {
    color: #e6e6e6;
}
.navbar-form {
    padding-top: 8px;
    color: #e6e6e6;
}

/* Link Effect: Curl Top Right */
.hvr-curl-top-right {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: translateZ(0);
  transform: translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
}
.hvr-curl-top-right:before {
  pointer-events: none;
  position: absolute;
  content: '';
  height: 0;
  width: 0;
  top: 0;
  right: 0;
  background: white;
  /* IE9 */
  background: linear-gradient(225deg, white 45%, #aaaaaa 50%, #cccccc 56%, white 80%);
  box-shadow: -1px 1px 1px rgba(0, 0, 0, 0.4);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: width, height;
  transition-property: width, height;
}
.hvr-curl-top-right:hover:before, .hvr-curl-top-right:focus:before, .hvr-curl-top-right:active:before {
  width: 25px;
  height: 25px;
}

.container-fluid {
    z-index:1;
}

img.bg {
  /* Set rules to fill background */
  min-height: 100%;
  min-width: 1024px;

  /* Set up proportionate scaling */
  width: 100%;
  height: auto;

  /* Set up positioning */
  position: fixed;
  top: 0;
  left: 0;
}
.parallax {
    z-index:1;
    width:100%;
    min-height:100%;
    height:100%;
}

.panel-info > .panel-heading {
    background-color: #D8562B;
    border-color: #D8562B;
}

.panel-info {
    border-color: #D8562B;
}

.panel-title {
    color: #e6e6e6;
}

.loginbox {
    margin-top: 60px;
}

.maincontent {
    padding-top: 60px;
    min-height: 100%;
    position: absolute;
    top: 0;
    background-color: #fff;
    padding-bottom: 65px;
}

.mainbox {
    background-color: #fff;
    width:80%;
    margin-left: auto;
    margin-right: auto;
    height: 100%;
    min-height: 100%;
}

.footer {
    margin: 0;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 60px;
    background-color: #000;
    z-index: 1;
}

/* Fix a couple things for mobile/low-res */

@media screen and (max-width: 768px) {
  img.bg {
    left: 50%;
    margin-left: -512px;   /* 50% */
  }
  .maincontent {
    width: 80%;
    left: 10%;
  }
}

/* Storefront styles */

.storefront_book_display {
    width: 200px;
    display: inline-block;
    text-align: center;
}

.storefront_book_title {
    font-size: 14px;
    display: block;
    font-weight: bold;
}

.storefront_book_author {
    font-size: 11px;
    display: block;
}
.storefront_add_to_cart {
    display: block;
    margin-top: 10px;
}

/* Book detail styles */
.detail_book_display {
    text-align: center;
    margin-top: 20px;
}
.detail_book_img {
    margin-bottom: 20px;
}
.detail_book_title {
    font-size: 20px;
    display: block;
    font-weight: bold;
}
.detail_book_author {
    font-size: 16px;
    display: block;
}
.detail_book_description {
    text-align: left;
    margin-top: 20px;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
}
.detail_book_reviews_title {
    margin-top: 20px;
    margin-bottom: 20px;
    font-size: 20px;
    display:block;
    font-weight: bold;
}
.detail_book_reviews_map {
    width: 500px;
    height: 300px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Cart Styles */
.cart_container {
		display: block;
		max-width: 750px;
		margin-left: auto;
		margin-right: auto;
}
.cart_item {
		width: 100%;
		margin-top: 20px;
		display: block;
		border-bottom: 1px solid black;
		padding-bottom: 20px;
}
.cart_listing {
		display: inline-block;
		width: 50%;
}
.cart_listing .title {
		display: block;
		font-weight: bold;
}
.cart_price {
		display: inline-block;
		text-align: right;
		width: 49%;
		vertical-align: top;
}
.cart_value {
		font-weight: bold;
}
.cart_quantity {
		display: block;
}
.cart_total {
		text-align: right;
		margin-top: 20px;
}
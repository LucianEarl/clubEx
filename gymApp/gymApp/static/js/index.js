function stripeElements() {

  stripe = Stripe('pk_test_51HjKsMEh7fsFCPRmVzdBFpqEvXOih6ICBXVTQ9fYriIDkRIr8gmNhAU8zrKp6QCfg7nz8qE3Ee7gy5Ni6cC38U6Q00RoL9O0Zm');
  //set subscribe button inactive until all form completed and validated
  document.getElementById("submit").disabled = true;

  if (document.getElementById('card-element')) {
    let elements = stripe.elements();
    // Card Element styles
    let style = {
    	base: {
    		color: "#32325d",
    		fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    		fontSmoothing: "antialiased",
    		fontSize: "18px",
    		"::placeholder": {
    			color: "#aab7c4"
    		}
    	},
    	invalid: {
    		color: "#fa755a",
    		iconColor: "#fa755a"
    	}
    };
    //Insert card element 
    card = elements.create('card', { style: style });
    card.mount('#card-element');
    //Set a focus on card for errors 
    card.on('focus', function () {
      let el = document.getElementById('card-errors');
      el.classList.add('focused');     
    });

    card.on('blur', function () {
      let el = document.getElementById('card-errors');
      el.classList.remove('focused');
    });

    card.on('change', function (event) {
      document.getElementById("submit").disabled = false;
      displayError(event);
    });
  }
};
// How to display errors
function displayError(event) { 
  let displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
   
  }
};

//Selecting the plan
function planSelect(name, price, priceId) {
  var inputs = document.getElementsByTagName('input');

  for(var i = 0; i<inputs.length; i++){
    inputs[i].checked = false;
    if(inputs[i].name== name){
      inputs[i].checked = true;
    };
  };
  //insert data into payment form from selection
  var n = document.getElementById('plan');
  var p = document.getElementById('price');
  var pid = document.getElementById('priceId');
  n.innerHTML = name;
  p.innerHTML = price;
  pid.innerHTML = priceId;
  //activate subscribe button 
  
  alert("X-Devs - testing\nGenuine card information cannot be used in test mode. Instead, use any of the following test card numbers, a valid expiration date in the future, and any random CVC number,any postal code with min 5 numbers to create a successful payment.\n 4242 4242 4242 4242\n5555 5555 5555 4444")
};




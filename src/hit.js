<!-- You must include this JavaScript file -->
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<!-- For the full list of available Crowd HTML Elements and their input/output documentation,
      please refer to https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html -->

<!-- You must include crowd-form so that your task submits answers to MTurk -->
<crowd-form answer-format="flatten-objects">

    <p>
      <strong>Instructions: </strong>
      Given an image of a comic book character, answer the following questions below.
    </p>

    <!-- Your image file URLs will be substituted for the "image_url" variable below 
          when you publish a batch with a CSV input file containing multiple image file URLs.
          To preview the element with an example image, try setting the src attribute to
          "https://s3.amazonaws.com/cv-demo-images/basketball-outdoor.jpg" -->

    <p><img src="${image_url}" style="max-width: 100%; max-height: 250px" /></p>

    <p>Have you seen this character before?</p>

    <crowd-radio-group name="character_seen">
        Yes
        <crowd-radio-button name="seen"></crowd-radio-button>
        No
        <crowd-radio-button name="not_seen"></crowd-radio-button>
    </crowd-radio-group>

    <p>
      How would you describe this character? 
      Please give 3 adjectives that you believe describe the character's physical appearance from the above image. 
    </p>

    <crowd-input label="Adjective 1" max-length="25" name="phys0" required></crowd-input>
    <crowd-input label="Adjective 2" max-length="25" name="phys1" required></crowd-input>
    <crowd-input label="Adjective 3" max-length="25" name="phys2" required></crowd-input>
    
    <p>
      Please give 3 adjectives that you believe describe the character's personality or persona from the above image. 
    </p>

    <crowd-input label="Adjective 1" max-length="25" name="pers0" required></crowd-input>
    <crowd-input label="Adjective 2" max-length="25" name="pers1" required></crowd-input>
    <crowd-input label="Adjective 3" max-length="25" name="pers2" required></crowd-input>
    
    <p>
      Please give 3 adjectives that you believe describe the emotions the character evokes from the above image. 
    </p>

    <crowd-input label="Adjective 1" max-length="25" name="emot0" required></crowd-input>
    <crowd-input label="Adjective 2" max-length="25" name="emot1" required></crowd-input>
    <crowd-input label="Adjective 3" max-length="25" name="emot2" required></crowd-input>
    
    <p>
      Please type the prompt word in the box below.
    </p>
    
    <crowd-input label="${prompt}" max-length="25" name="type_test" required></crowd-input>
    
    <p>
      You must respond to each question before you submit.
    </p>
    
</crowd-form>
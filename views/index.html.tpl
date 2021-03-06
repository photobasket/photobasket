%include views/_header.html.tpl

<nav class="navbar navbar-inverse">
  <div class="container">
    <div class="navbar-header">
      <img src="/img/Logo.svg" class="navbar-brand">
    </div>
  </div>
</nav>

<div class="container">
  <div class="row">
    <div class="col-xs-12">
      <img src="/img/happy-family.jpg" style="width: 100%;">
    </div>
  </div>

  <div class="row">
    <div class="col-md-offset-4 col-md-8">
      <h1 class="heading">Create your own PhotoBasket</h1>
      <p>
        To create a your own PhotoBasket simply give it a name and type in your email address. That's it. You can then invite friends
        to share their pictures and upload your own. You choose who get's access. Your pictures, your rules.
      </p>
      <form>
        <div class="input-group">
          <label class="control-label" for="name">Name</label>
          <input class="form-control" type="text" id="name" name="name">
        </div>
        <div class="input-group">
          <label class="control-label" for="email">Email</label>
          <input class="form-control" type="email" id="email" name="email">
        </div>
        <input type="submit" class="btn btn-primary" value="Create your PhotoBasket">
      </form>
      <h1 class="heading">About</h1>
      <p>
        This PhotoBasket server is operated by <a href="mailto:john.doe@example.com">John Doe</a>. Learn how to get <a href="">your own PhotoBasket</a>.
      </p>
    </div>
  </div><!--/.row-->
</div><!--/.container-->

% include views/_footer.html.tpl

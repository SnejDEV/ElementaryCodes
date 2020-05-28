#input email
email=input("Enter e-mail: ").strip()
#username_proc
username=email[:email.index('@')]
#domain_name
domain=email[email.index('@')+1:email.index('.')]
#top-level domain
tlDomain=email[email.index('.'):]
#output
print("""Username: {0}
Domain: {1}
Top-level Domain: {2}""".format(username,domain,tlDomain))

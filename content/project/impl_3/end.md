[Back (Implementation III)](../impl_3/end.md)

# Final thoughts

Now, in a real project, things get stressful. We have to prove that our design is ready for the future. Requirements change and our design must be able to react flexibly to these requirements.

What could these changing requirements be?

Try to implement one or even all of the following requirement changes in your project:

- Database technology needs to change (e.g. from NoSQL to PostgreSQL).
- The transmission protocol of the input interface changes from TCP to UDP
- The JSON format gets new entries like edition or purchase date
- An algorithm is to be implemented that automatically calculates the sales price. The following formula can be used: Purchase price * (1.2 - number of books of this edition in stock * 0.05). However, the sales price must not be less than the purchase price * 1.1.
- Can you find a better formula for change price and switch the price calculation depending on the current date? (think about christmas sales or black friday)
- The output interface must scale up by 10 times in terms of throughput

Are you already starting to sweat? ;-)

I hope you had fun with this project and could try out and learn something new.

Best regards
Alex


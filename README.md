# MatchingSimple
Implementation of Matching algorithm used by NRMP

The algorithm is implemented based on the following paragraph of this paper:"The Redesign of the Matching Market for American Physicians: Some Engineering Aspects of Economic Design"
https://web.stanford.edu/~alroth/papers/rothperansonaer.PDF

"In the worker-proposing version of the algorithm, each worker begins by applying for the position at the top of her preference list. Each firm rejects any unacceptable candidates, and if it has q positions it temporarily holds the (up to) q most-preferred applications it has so far received and rejects the rest. A candidate who is rejected at any step of the algorithm next applies to her next-highest-ranked position (if any remain) among those not yet applied to. The algorithm stops at any step in which no new applications are made, at which point each worker is matched to the firm (if any) holding her application."

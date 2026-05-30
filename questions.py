# questions.py
import random

RAW_QUESTION_BANK = [
    # === UNIT 1: AGGREGATE PLANNING OPTIMISATION ===
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "What is the core strategic horizon and goal of Aggregate Production Planning (APP)?",
        "options": ["Daily short-term sequencing of products on specific manufacturing work centers", "Medium-term planning matching demand and supply over 3 to 18 months, targeting overall production levels", "Long-term facility design and macro location planning over 5 to 10 years"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "Which mathematical approach is standard for modeling decision structures like workforce adjustments, inventory costs, backorders, and multi-product capacities simultaneously?",
        "options": ["Mixed Integer Linear Programming (MILP)", "Simple Moving Average calculations", "Greedy Shortest Processing Time rules"],
        "correct": 0
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "In a standard MILP for Aggregate Planning, what type of variable represents workforce size or binary firing/hiring triggers?",
        "options": ["Continuous non-negative variables", "Integer or Binary decision variables", "Unconstrained stochastic inputs"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "In Aggregate Production Planning, what does an inventory balance constraint state?",
        "options": ["Ending Inventory = Beginning Inventory + Production - Demand", "Ending Inventory = Beginning Inventory - Firing + Hiring", "Ending Inventory = Demand - Capacity + Backorders"],
        "correct": 0
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "Which of the following would be an example of an operational structural constraint added to a customized corporate aggregate planning model?",
        "options": ["Limiting workforce capacity changes between consecutive planning periods to an absolute variance limit", "Ignoring setup costs across all scheduling profiles", "Optimizing the sequence of parts inside an assembly station"],
        "correct": 0
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "What tool or framework is recommended in the MUCEIM slides to run and evaluate your developed Aggregate Planning MILP code configurations?",
        "options": ["Excel Goal Seek exclusively", "Pyomo mathematical modeling language in Python", "MATLAB Simulink blocks"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "A pure 'chase strategy' in Aggregate Planning focuses primarily on doing what?",
        "options": ["Maintaining constant production rates and absorbing demand changes with inventory cushions", "Adjusting production output capacity and workforce levels dynamically to match fluctuating demand profiles", "Subcontracting 100% of the baseline manufacturing capacity requirements"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "A pure 'level strategy' in Aggregate Production Planning is defined by which behavior?",
        "options": ["Altering workforce limits dynamically every month to closely mirror incoming raw demand orders", "Maintaining a steady production rate and workforce size, using inventory/backorders to absorb demand fluctuations", "Varying machine configuration times daily to accommodate low setup thresholds"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "What objective function direction is typically used when formulating an optimization model for Aggregate Production Planning?",
        "options": ["Maximization of raw inventory stock levels", "Minimization of global system operating costs (production, inventory, labor adjustments, backorders)", "Minimization of the number of active production variants available"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "What data is categorized as an INPUT parameter rather than a decision variable in an APP model?",
        "options": ["Monthly demand forecasts, production capacities, and specific resource cost structures", "The quantity of products to manufacture during period t", "The number of temporary workers to hire at the start of period t"],
        "correct": 0
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "Which of the following is considered an emerging future direction for Aggregate Production Planning frameworks?",
        "options": ["Elimination of mathematical modeling in favor of manual spreadsheets", "Real-time adaptive planning systems integrated with digital twins and IoT data for dynamic adjustment", "Transitioning all medium-term aggregates exclusively to short-term dispatcher rules"],
        "correct": 1
    },
    {
        "unit": "Unit 1: Aggregate Planning",
        "question": "What is a main limitation of using traditional linear programming models for Aggregate Planning without integer components?",
        "options": ["They struggle to represent fractional human operators or discrete binary configurations accurately", "They cannot compute minimum cost alternatives", "They are too computationally heavy for modern systems"],
        "correct": 0
    },

    # === UNIT 2: MATERIALS REQUIREMENT PLANNING OPTIMISATION ===
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What is the primary objective of the Materials Requirement Planning (MRP) framework?",
        "options": ["To map out a corporate macro layout design", "To translate a Master Production Schedule (MPS) into time-phased component net requirements and planned order releases", "To handle continuous sequencing of complex multi-variant single lines"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "Which structural input describes the exact hierarchical relation and quantities of raw items or sub-assemblies needed to make a final product?",
        "options": ["The Precedence Matrix", "The Bill of Materials (BOM)", "The Machine Route Matrix"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "In MRP explosion arithmetic, how are Net Requirements calculated?",
        "options": ["Net Requirements = Gross Requirements - Scheduled Receipts - Available Inventory from previous period", "Net Requirements = Gross Requirements + Order Costs + Holding Costs", "Net Requirements = Planned Order Releases * Lead Time Variance"],
        "correct": 0
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What does 'Lead Time Offset' or time-phasing mean in an MRP calculation engine?",
        "options": ["Advancing Planned Order Receipts into past periods as safety backups", "Determining Planned Order Releases by shifting Planned Order Receipts backward in time based on item lead time", "Multiplying total inventory values by historical holding costs"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "Which lot-sizing heuristic balances total ordering and holding costs by selecting lots that minimize costs per unit step-by-step?",
        "options": ["Lot-for-Lot (L4L)", "Minimum Unit Cost (MUC)", "Silver-Meal Sequence Limit"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What does the abbreviation 'MTC' refer to within MRP lotification techniques?",
        "options": ["Minimum Total Cost lot sizing", "Maximum Time Capacity constraint", "Multi-Threaded Computation rule"],
        "correct": 0
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What does the abbreviation 'SMM' signify in the context of advanced lot-sizing calculations?",
        "options": ["Stochastic Machine Mapping", "Silver-Meal Method", "Single Model Manufacturing balancing"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What is the fundamental property of a 'Lot-for-Lot' (L4L) policy in MRP environments?",
        "options": ["It groups all historical yearly demand profiles into single giant production runs", "It makes planned order quantities exactly equal to the net requirements of each individual period", "It maintains fixed inventory safety cushions of at least 100 units at all times"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What is an 'MRP Explosion'?",
        "options": ["A physical failure of manufacturing resources during line runtime operations", "The step-by-step logic calculating lower-level component gross requirements from higher-level parent planned order releases", "An error in Pyomo code compiling constraints improperly"],
        "correct": 1
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What structural challenge occurs if you modify order costs or holding costs within an MRP test data model?",
        "options": ["It changes the optimal grouping of periods under cost-optimizing lotification heuristics like MUC, MTC, or SMM", "It invalidates the parent-child relationships defined inside the BOM structure", "It causes Pyomo integer bounds to yield infeasible mathematical vectors"],
        "correct": 0
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "Which elements are necessary components to execute a baseline MRP execution run?",
        "options": ["BOM structural graphs, inventory statuses, lead times, and Master Production Schedules", "Sequence-dependent setup matrices and Tabu lists", "Cycle times and workstation line layout assignments"],
        "correct": 0
    },
    {
        "unit": "Unit 2: Materials Requirement Planning",
        "question": "What represents a modern extension path for current traditional MRP frameworks?",
        "options": ["Using manual calculations to reduce computational complexity", "Integration with AI/ML for demand forecasting and real-time connectivity with IoT architectures", "Eliminating time-phased records entirely to prioritize simple average lotting"],
        "correct": 1
    },

    # === UNIT 3: ECONOMIC LOT SCHEDULING OPTIMISATION ===
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What trade-off defines the Economic Lot Scheduling Problem (ELSP) in multi-product environments?",
        "options": ["Balancing line balance efficiency with workstation assignment cycles", "Balancing setup costs, inventory holding costs, and potential backlogs across multiple products on a shared machine", "Balancing employee hiring variables with aggregate firing trends over multiple years"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "Which heuristic algorithm prioritizes production items step-by-step based on the product that will run out of available stock first?",
        "options": ["Monden's Method", "Run-Out Method", "Johnson's Two-Machine Rule"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What logical calculation error can happen in a greedy Run-Out Method implementation if an item is sequenced twice consecutively?",
        "options": ["The algorithm crashes due to zero division errors", "An extra setup time/cost might be counted that should not be applied since the machine is already set up for that item", "The total cycle time becomes mathematically infinite"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "When solving ELSP with a Genetic Algorithm, what represents a smarter stopping condition than just reaching a max loop iteration counter?",
        "options": ["Stopping when total inventory matches raw demand volumes exactly", "Monitoring population fitness metrics and stopping when convergence indicates no meaningful improvements occur over several generation loops", "Stopping the code the instant an infeasible individual sequence is generated"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What profiles are typically plotted to visualize population convergence traits in an ELSP Genetic Algorithm simulation?",
        "options": ["Minimum, average, and maximum fitness progression values over generations", "The processing times of jobs split across a set of physical workstations", "The level of hiring variances across multiple planning horizons"],
        "correct": 0
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What parameters form the basic foundation of ELSP mathematical scheduling profiles?",
        "options": ["Product demand rates, production capacity rates, setup costs, and unit holding values", "Precedence graphs, task idle variables, and workstation counts", "Workforce hiring upper bounds, firing variables, and aggregate storage limits"],
        "correct": 0
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "Why is the ELSP considered computationally challenging compared to the standard single-item Economic Order Quantity (EOQ) model?",
        "options": ["Because multiple products contend for production time on the same shared manufacturing asset without overlapping", "Because it uses continuous linear parameters with no setup dependencies", "Because it is solved exclusively by manual mathematical reduction techniques"],
        "correct": 0
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What is a main characteristic of evolutionary metaheuristics like Genetic Algorithms when applied to ELSP optimization?",
        "options": ["They evaluate single deterministic sequences and never utilize random mutation patterns", "They explore solutions using a population of chromosomes, finding near-optimal solutions for complex search spaces", "They guarantee finding the absolute mathematical optimum within 2 simulation iterations"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What is the primary definition of 'Run-Out Time' for a specific product item in a warehouse environment?",
        "options": ["The time required to change a machine configuration over to a new tool setup", "The estimated duration until current inventory is fully depleted based on active demand consumption rates", "The total physical lead time of a sub-component listed inside the master BOM structure"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What is a common extension of the basic ELSP formulation?",
        "options": ["Eliminating setup variables completely", "Incorporating sequence-dependent setups, multi-machine environments, and stochastic demand variability", "Restricting all products to be produced in identical fixed batches of 1 unit"],
        "correct": 1
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "In a Genetic Algorithm for scheduling, what does the term 'chromosomal representation' refer to?",
        "options": ["The specific data structure encoding a candidate production sequence solution within the population", "The physical hardware layout map of a plant floor automation station", "The total financial investment required to purchase raw materials"],
        "correct": 0
    },
    {
        "unit": "Unit 3: Economic Lot Scheduling",
        "question": "What does a fitness function do within an ELSP Genetic Algorithm optimization environment?",
        "options": ["It tracks how fast an operator executes tool changes on the production floor", "It measures the overall structural cost performance of a specific candidate sequence to drive evolutionary selection", "It counts the total number of lines inside the Pyomo source code code structure"],
        "correct": 1
    },

    # === UNIT 4: FLOW SHOP SCHEDULING OPTIMISATION ===
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What is the key defining layout feature of a traditional Flow Shop production environment?",
        "options": ["Jobs follow individual routing patterns through various work centers", "All jobs must pass through all available processing machines in the exact same technological order sequence", "Resources move continuously around stationary stationary product units"],
        "correct": 1
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "Which algorithm provides an exact mathematical optimal sequence solution for a 2-machine Flow Shop problem to minimize total makespan ($C_{max}$)?",
        "options": ["Monden's Method", "Johnson's Algorithm", "The Largest Candidate Rule"],
        "correct": 1
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "How can Johnson's Algorithm principles be generalized to approximate M-machine Flow Shop scenarios?",
        "options": ["By grouping components into fictitious surrogate machines to solve routing pairs, or generating heuristic sequences based on processing times", "By transforming the flow shop directly into an unconstrained single linear function", "By using the Hungarian matrix method to allocate tasks to unique resources"],
        "correct": 0
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What exact Branch & Bound solution strategy is utilized to find guaranteed optimal scheduling sequences for Flow Shop problems?",
        "options": ["Lomnicki's Method", "The Hungarian Assignment Method", "The Run-Out Time Search Heuristic"],
        "correct": 0
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What structural condition occurs during the execution of Johnson's generalized algorithm when processing time ties occur?",
        "options": ["The code encounters an unresolvable error and aborts immediately", "Multiple alternative optimal or near-optimal job sequences emerge from the decision framework", "The problem changes into a Job Shop schedule model"],
        "correct": 1
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What represents the standard objective metric minimized in basic Flow Shop optimization models?",
        "options": ["Total employee hiring variances across consecutive periods", "The makespan ($C_{max}$), which is the total completion time of the entire set of jobs", "The number of parent items listed in a product's BOM sheet"],
        "correct": 1
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "If Job A requires 2 hours on Machine 1 and 5 hours on Machine 2, while Job B requires 6 hours on Machine 1 and 3 hours on Machine 2, what sequence does Johnson's 2-machine rule generate?",
        "options": ["Sequence Job B first, then Job A (B -> A)", "Sequence Job A first, then Job B (A -> B)", "Both sequences provide identical makespan outcomes"],
        "correct": 1
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What is a major trade-off between Lomnicki's exact Branch & Bound method and heuristic setups like Johnson's approximations for large problems?",
        "options": ["Lomnicki's method guarantees absolute optimality but suffers from exponential computational growth, whereas heuristics provide fast solutions but cannot guarantee optimality", "Heuristics require more processing time and memory than exact Branch & Bound variants", "Lomnicki's approach only works if machine processing time equals zero"],
        "correct": 0
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What parameters must be supplied to execute a Flow Shop Scheduling evaluation script?",
        "options": ["The matrix of operation processing times for each job on each consecutive machine", "The aggregate resource capacity bounds and workforce hiring costs", "The structural parent-component relationships and lead times from the BOM"],
        "correct": 0
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "In Flow Shop context, what is a 'Permutation Flow Shop'?",
        "options": ["A line where the processing order of jobs can change arbitrarily on every single machine", "A subset where all machines process the set of jobs in the exact same sequence order", "A scheduling structure solved exclusively by the Hungarian Method matrix operations"],
        "correct": 1
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What describes a key aspect of executing a Branch & Bound algorithm like Lomnicki's method?",
        "options": ["Systematic exploration of a state tree while using bounds to prune unpromising sequence branches early", "Using random mutation strings to explore candidate solutions across dozens of parallel generations", "Greedily choosing tasks that possess the largest number of total structural downstream successors"],
        "correct": 0
    },
    {
        "unit": "Unit 4: Flow Shop Scheduling",
        "question": "What is an emerging development path for modern industrial flow shop scheduling system design?",
        "options": ["Returning exclusively to manual scheduling matrices", "Adaptive hybrid metaheuristics linked with digital twins and cloud execution for autonomous re-scheduling", "Converting all multi-machine configurations into isolated single-item setups"],
        "correct": 1
    },

    # === UNIT 5: JOB SHOP SCHEDULING OPTIMISATION ===
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What differentiates a Job Shop scheduling problem from a traditional Flow Shop scheduling problem?",
        "options": ["Job Shop routing is completely uniform; all items follow an identical path across machines", "Each job has a customized and independent machine routing path sequence with varying operation times", "Job Shops do not include setup or processing time dependencies"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What does the abbreviation 'PDR' stand for in operational Job Shop scheduling terminology?",
        "options": ["Priority Dispatching Rules", "Parametric Digital Routing", "Product Demand Ratio"],
        "correct": 0
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "Which of the following is an example of a common Priority Dispatching Rule (PDR) used on a job shop floor?",
        "options": ["Munden's sequence rule", "Shortest Processing Time (SPT)", "The Hungarian matrix reduction method"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What metaheuristic technique uses memory structures called 'Tabu lists' to escape local optima in Job Shop optimization?",
        "options": ["Genetic Algorithms", "Tabu Search (TS)", "Branch & Bound tree search"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What famous reference instances are utilized in the Unit 5 assignment to benchmark PDR and Tabu Search algorithm implementations?",
        "options": ["Monden automotive lines", "Taillard's benchmark instances (specifically the 8taxx9 sets)", "Silver-Meal lotization profiles"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What utility must be coded to test Taillard instances inside a custom PDR/TS evaluation engine?",
        "options": ["An automated matrix text converter to transform Taillard's instance data formats into compatible internal application data structures", "A workforce generator that calculates hiring and firing costs", "An MRP explosion loop that converts requirements into parent BOM records"],
        "correct": 0
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What is a main role of the 'Tabu List' mechanism within a local search metaheuristic framework?",
        "options": ["To store the absolute best global coordinates found during the history of an entire optimization run", "To temporarily forbid recently visited moves or solutions, preventing the algorithm from cycling in local optima", "To filter out structurally infeasible parent configurations before code execution runs"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What metric represents the benchmark target often extracted from the 'UB' column of known Taillard solutions?",
        "options": ["The Upper Bound value of the optimal makespan ($C_{max}$)", "The total operational holding cost index", "The workstation line efficiency percentage"],
        "correct": 0
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What is a major operational limitation of using simple Priority Dispatching Rules (PDR) for complex Job Shop scheduling?",
        "options": ["They are too slow to run on modern computers", "They are greedy and short-sighted, frequently yielding solutions far from the global mathematical optimum", "They cannot process jobs that have more than two distinct manufacturing operations"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What input details are necessary to properly define a Job Shop Scheduling problem instance?",
        "options": ["The customized sequence of machines required by each job and the processing time for each distinct operation", "The aggregate safety stock targets and monthly warehouse holding cost coefficients", "The number of direct successors linked to each task within a line precedence graph"],
        "correct": 0
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "In Job Shop modeling, what does 'neighborhood structure' mean within local search frameworks like Tabu Search?",
        "options": ["The geographic physical layout proximity of tools inside a production plant", "The set of candidate schedules generated by applying small, well-defined changes (like swapping two operations) to a current schedule", "The list of structural suppliers situated near an assembly warehouse"],
        "correct": 1
    },
    {
        "unit": "Unit 5: Job Shop Scheduling",
        "question": "What is a primary target of advanced future research directions in Job Shop Scheduling mentioned in the slides?",
        "options": ["Transitioning entirely back to manual scheduling visual aids", "AI-assisted scheduling via deep reinforcement learning and multi-objective optimization for efficiency and energy use", "Replacing discrete shop layouts with continuous uniform flow lines exclusively"],
        "correct": 1
    },

    # === UNIT 6: JOB-RESOURCE ASSIGNMENT OPTIMISATION ===
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What is the primary decision objective in an Ordinary Job-Resource Assignment Problem?",
        "options": ["To determine the sequence of operations on a continuous flow line", "To assign a set of individual jobs to an equal number of distinct resources on a one-to-one basis to minimize total cost or time", "To establish aggregate employee hiring bounds over multi-period horizons"],
        "correct": 1
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What classical, exact polynomial-time algorithm solves the Ordinary Assignment Problem optimally with an $O(n^3)$ computational complexity?",
        "options": ["Lomnicki's Branch & Bound Method", "The Hungarian Method", "The Run-Out Method Heuristic"],
        "correct": 1
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What type of decision variable is used to formulate an Ordinary Job-Resource Assignment model in a Mixed Integer Linear Program?",
        "options": ["Continuous variables between 0.0 and 100.0", "Binary decision variables ($x_{ij} \in \{0, 1\}$)", "Unbounded stochastic variables"],
        "correct": 1
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What structural constraints define an Ordinary Job-Resource Assignment mathematical model?",
        "options": ["Each job must be assigned to exactly one resource, and each resource must be assigned to exactly one job", "The total cycle time of an assignment cannot exceed workstation task counts", "The production volume must equal the time-phased component gross requirements"],
        "correct": 0
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What differentiates a Generalised Assignment Problem from an Ordinary Assignment Problem?",
        "options": ["The Generalised Assignment variant removes all resource capacity parameters entirely", "Resources can have capacity limitations that allow them to accept multiple job assignments simultaneously, rather than a strict one-to-one mapping", "It can only be solved using manual matrix reduction heuristics"],
        "correct": 1
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "In the Unit 6 task assignment, how should you evaluate and analyze your assignment model solutions?",
        "options": ["By manually guessing alternative pairs", "By generating dataset files and comparing Hungarian Method outputs with exact MILP solver results in Python", "By importing the data into an aggregate planning Pyomo matrix framework"],
        "correct": 1
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What constitutes the objective function configuration for a standard Job-Resource Assignment model?",
        "options": ["Minimizing the total sum of assignment costs or times across all chosen job-resource links", "Maximizing the idle variances between different active factory sectors", "Minimizing the total number of items listed inside an active BOM diagram"],
        "correct": 0
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What core matrix operations are executed when performing manual reduction loops within the Hungarian Method?",
        "options": ["Row and column cost reduction subtractions to identify an optimal set of zero-cost assignments", "Multiplying job processing speeds by workforce hiring costs", "Adding parent safety margins to component net requirements tables"],
        "correct": 0
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "If a cost matrix is not square (the number of jobs does not equal the number of resources) in an ordinary assignment problem, how is it pre-processed?",
        "options": ["The problem is flagged as mathematically infeasible and aborted", "Dummy rows or columns with zero or highly penalized costs are introduced to balance the matrix structure", "The smallest jobs are combined until the matrix balances"],
        "correct": 1
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What parameter models resource consumption when transitioning an assignment problem from ordinary to generalized?",
        "options": ["A resource capacity limit alongside a parameter defining how much of that capacity a specific job consumes", "A sequence-dependent tool configuration setup time matrix", "An aggregate monthly workforce hiring adjustment penalty coefficient"],
        "correct": 0
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What tool can solve the assignment problem using its linear programming relaxation without needing explicit integer branch steps?",
        "options": ["The problem possesses a totally unimodular constraint matrix structure, which guarantees integer solutions under standard LP solvers", "The problem is highly non-linear and cannot be processed by LP structures", "The model relies entirely on randomized Tabu local search memory patterns"],
        "correct": 0
    },
    {
        "unit": "Unit 6: Job-Resource Assignment",
        "question": "What represents a modern future extension for assignment models in industry?",
        "options": ["Relying exclusively on non-computerized ledger lists", "Robust/stochastic optimization models under uncertainty and graph neural networks for assignment learning patterns", "Forcing all jobs to utilize identical machine processing times regardless of complexity"],
        "correct": 1
    },

    # === UNIT 7: MIXED MODEL SEQUENCING OPTIMISATION ===
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What is the primary operational challenge in Mixed-Model Sequencing Problems (MMSP)?",
        "options": ["Determining the long-term location layout parameters of a plant floor", "Determining the optimal line sequence of different product variants on a single assembly line to balance component consumption and prevent line stoppages", "Exploding parent demand figures into lower-level sub-component requirements sheets"],
        "correct": 1
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "Which heuristic framework is famously applied to manage mixed-model sequencing constraints on automotive assembly lines?",
        "options": ["Lomnicki's Branch & Bound Method", "Monden's Method (Toyota Production System approach)", "The Hungarian Assignment Matrix Rule"],
        "correct": 1
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "When optimizing MMSP via a Genetic Algorithm, what does Option A for chromosome encoding define?",
        "options": ["Genes are coded directly as product identity numbers within the sequence chain", "Genes represent abstract sequence index parameters requiring deep secondary conversion loops", "Genes represent workforce capacity hiring variations across multi-period windows"],
        "correct": 0
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What advantage can Option A chromosome encoding (direct product numbers) offer over sequence position encoding?",
        "options": ["It increases code complexity and run times", "It can evaluate chromosome tracking metrics more quickly and provide better results in less computation time", "It entirely removes the need to calculate part consumption levels"],
        "correct": 1
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What optional structural parameter can be introduced to model sequencing preferences, such as keeping cars of the same color close together?",
        "options": ["Component net requirement offsets", "Attraction energy or setup grouping metrics in specific component features", "Workforce structural adjustment variance factors"],
        "correct": 1
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What is a core objective of Monden's Method in a mixed-model assembly line setup?",
        "options": ["To maximize total raw warehouse inventory volumes", "To smooth the consumption rate of different components over time, keeping it as constant and close to target levels as possible", "To isolate work centers from one another using giant inventory buffers"],
        "correct": 1
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What industry scenario heavily relies on effective Mixed-Model Sequencing Optimization implementations?",
        "options": ["High-volume mass customization environments like modern automotive assembly lines", "Traditional single-product continuous chemical processing plants", "Purely agricultural seasonal harvesting resource operations"],
        "correct": 0
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What happens if a mixed-model sequence is poorly planned and piles up high-workload variants consecutively?",
        "options": ["The line experiences work overloads, stations exceed their cycle time limits, and the line may stop", "The total demand volume automatically shrinks to fit line capacities", "The problem converts into an ordinary assignment problem profile"],
        "correct": 0
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What baseline parameters must be known to formulate an MMSP sequencing evaluation script?",
        "options": ["The list of product variants, their production quantities, and the specific component requirements per product model", "The employee hiring and firing cost functions across consecutive years", "The total downstream task successors listed in a line graph template"],
        "correct": 0
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "In a Genetic Algorithm for MMSP, what do crossover operations do?",
        "options": ["They mathematically prove that a candidate sequence represents the absolute global minimum cost solution", "They combine sub-sequences from two parent chromosomes to produce new offspring sequences that inherit their scheduling traits", "They delete half of the product variants to speed up optimization runs"],
        "correct": 1
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What is a main disadvantage of evaluating giant MMSP instances with exact linear programming solvers?",
        "options": ["The combinatorial search space grows exponentially, making exact methods too slow for real-time operational sequencing decisions", "Linear solvers can only compute zero-cost alternatives", "LP models are unable to process multi-product data inputs"],
        "correct": 0
    },
    {
        "unit": "Unit 7: Mixed Model Sequencing",
        "question": "What represents an emerging trend in Mixed-Model Sequencing optimization research?",
        "options": ["Eliminating computer modeling loops entirely", "Hybrid AI-optimization frameworks that combine evolutionary algorithms with reinforcement learning for adaptive real-time sequencing", "Enforcing strict batching of identical items to eliminate mass customization entirely"],
        "correct": 1
    },

    # === UNIT 8: ASSEMBLY LINE BALANCING OPTIMISATION ===
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What is the primary objective of the Assembly Line Balancing Problem (ALBP)?",
        "options": ["To maximize the total raw inventory held between adjacent factory zones", "To allocate discrete manufacturing tasks across a set of workstations to minimize idle time and balance workloads, while respecting cycle time and precedence constraints", "To schedule individual jobs across independent customized routing paths"],
        "correct": 1
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What key operational boundary condition dictates that the sum of task times assigned to any single workstation cannot exceed a specific maximum threshold?",
        "options": ["The Lead Time Offset constraint", "The Cycle Time constraint ($C$)", "The Firing Variance parameter"],
        "correct": 1
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What do precedence constraints represent within an Assembly Line Balancing problem structure?",
        "options": ["The financial cost hierarchy of alternative equipment upgrades", "The mandatory technological sequencing order requiring certain tasks to be fully completed before other downstream tasks can begin", "The ratio of permanent workers versus temporary operators"],
        "correct": 1
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "Which heuristic algorithm serves as the classic baseline constructive method for ALBP by sorting tasks by processing times?",
        "options": ["The Run-Out Method", "The Largest Candidate Rule (LCR)", "Monden's Heuristic Method"],
        "correct": 1
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What rule prioritizes tasks based on the number of downstream successors they unlock in the precedence graph?",
        "options": ["The Followers First priority rule", "The Shortest Processing Time dispatching rule", "The Hungarian matrix allocation rule"],
        "correct": 0
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "How is Line Efficiency ($\eta$) calculated in an Assembly Line Balancing problem evaluation?",
        "options": ["$\eta = \sum t_i / (m \cdot C)$, where $t_i$ are task times, $m$ is the number of stations, and $C$ is the cycle time", "$\eta = \text{Total Production Volume} / \text{Workforce Hiring Cost}$", "$\eta = \text{Total Successors} / \text{Total Idle Time}$"],
        "correct": 0
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What does a constructive heuristic for ALBP do when an eligible task does not fit within the remaining time of the current active workstation?",
        "options": ["It closes the current workstation and opens a new workstation to assign the task", "It shortens the task's processing time until it fits", "It violates the precedence rule to place the task elsewhere"],
        "correct": 0
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What constitutes the mathematical metric known as Total Idle Time ($I$) across an balanced assembly line?",
        "options": ["The sum across all workstations of the cycle time minus the actual total station time ($I = \sum (C - T_s)$)", "The time an operator spends executing setup configurations", "The total lead time shift recorded inside the parent BOM sheet"],
        "correct": 0
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What is the difference between counting all direct and indirect successors versus counting only direct successors in precedence priority rules?",
        "options": ["Counting all direct and indirect successors maps the entire remaining downstream path length, whereas counting only direct successors focuses strictly on the immediate next tasks unlocked", "Counting indirect successors causes the model to become linear and unconstrained", "There is no mathematical or logical difference between these two approaches"],
        "correct": 0
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "What method serves as the exact benchmark to evaluate the solution quality of constructive heuristics like LCR or Followers First?",
        "options": ["The greedy Run-Out method profile", "An exact Mixed Integer Linear Programming (MILP) model formulation solved to optimality", "A manual row-reduction Hungarian matrix template"],
        "correct": 1
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "In ALBP, what condition defines whether a task is 'eligible' to be assigned to a workstation?",
        "options": ["All of its structural predecessor tasks have already been fully assigned, and its task time fits within the current workstation's remaining time", "The task has the longest processing time among all items in the database", "The task is listed as a parent component inside the master MRP explosion chart"],
        "correct": 0
    },
    {
        "unit": "Unit 8: Assembly Line Balancing",
        "question": "Who is the teacher listed on the cover slides for Unit 8: Assembly Line Balancing Optimisation?",
        "options": ["Raul Poler", "Beatriz Andres", "Manuel Rodilla"],
        "correct": 1
    },

    # === UNIT 9: RESOURCE ALLOCATION OPTIMISATION ===
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What distinguishes Resource Allocation Optimisation (Unit 9) from Assembly Line Balancing (Unit 8)?",
        "options": ["Unit 8 balances workloads across production workstations, whereas Unit 9 involves the effective deployment of organizational resources (people, skills, budgets, equipment) across different functions and activities", "Unit 9 focuses exclusively on sequence-dependent product setups", "Unit 8 is solved by exact solvers, whereas Unit 9 can only be modeled with greedy heuristics"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What specific heuristic scheduling method is introduced in Unit 9 to optimize resource deployment?",
        "options": ["The Monden Assembly Line Sequencing Method", "The Manpower Scheduling Method (MSM)", "The Johnson Two-Machine Formulation"],
        "correct": 1
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What task is assigned in the Unit 9 homework to test and analyze the performance of resource allocation algorithms?",
        "options": ["Coding a synthetic data generator to evaluate random problems across small, medium, large, and very large datasets", "Developing an exact Hungarian matrix converter for Taillard instances", "Modifying a Genetic Algorithm to change option A chromosome representations"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What solver configuration can be specified to ensure an exact MILP model finds a solution for large resource allocation datasets within a reasonable time?",
        "options": ["Setting a specific optimality GAP percentage value", "Disabling integer branching steps entirely to run an unconstrained continuous linear relaxation", "Forcing the solver to run for a minimum of 24 hours without stopping"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What metrics are compared when evaluating the performance of the Manpower Scheduling Method (MSM) against an exact MILP model solution?",
        "options": ["Solution optimality (objective value performance) and total computational execution time", "The total number of parent levels inside an active BOM diagram", "The line efficiency percentage and individual task idle time values"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What resources are typically optimized within a Unit 9 Resource Allocation framework?",
        "options": ["People, cross-functional skills, project teams, budgets, and technical equipment", "Product variants tracking along a single assembly conveyor line", "Parent items and component lead times listed in a time-phased spreadsheet"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "Who are the instructors responsible for delivering Unit 9: Resource Allocation Optimisation?",
        "options": ["Raul Poler exclusively", "Beatriz Andres & Raul Poler jointly", "Beatriz Andres exclusively"],
        "correct": 1
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What is a main goal of combining simulation-based optimization with reinforcement learning in advanced resource allocation research?",
        "options": ["To eliminate the use of computer models in favor of manual schedules", "To enable dynamic resource scheduling that adapts in real time to workforce and equipment variability", "To ensure all tasks follow a strict, unalterable technological sequence order"],
        "correct": 1
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What does a 'synthetic data generator' do in the context of your resource allocation homework task?",
        "options": ["It generates random test problems bounded between a minimum and maximum number of tasks and resources to benchmark algorithm performance", "It automatically copies solution code files from online repositories", "It explodes master production schedules into lower-level component net requirements"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What happens to the computational performance of an exact MILP solver as the number of tasks and resources scales up to 'very large' datasets?",
        "options": ["The computation time drops to near zero due to linear relaxation traits", "The combinatorial search space expands exponentially, causing the solver to require a long time to prove absolute mathematical optimality", "The solver automatically switches to the Hungarian Method to bypass the capacity constraints"],
        "correct": 1
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What is a primary focus of resource allocation optimization in project management contexts?",
        "options": ["Allocating skilled staff from different departments to support multiple projects based on priority and availability constraints", "Balancing task times evenly across a set of physical workstations along a moving conveyor line", "Minimizing sequence-dependent tool setup times on a shared machine asset"],
        "correct": 0
    },
    {
        "unit": "Unit 9: Resource Allocation",
        "question": "What structural file format must be used to submit your completed homework tasks for evaluation to PoliformaT?",
        "options": ["A raw uncompressed folder structure containing Python files", "A single ZIP file containing your report template (in both DOCX and PDF formats) alongside your Python source code files", "An Excel spreadsheet file containing your raw output matrices"],
        "correct": 1
    },

    # === ADDITIONAL REINFORCEMENT INTEGRATION QUESTIONS ===
    # Unit 1 Multipliers
    {"unit": "Unit 1: Aggregate Planning", "question": "What does a negative value in a raw linear programming optimization result typically indicate if bounds are omitted?", "options": ["An impossible or structurally invalid operational state, requiring non-negativity variable constraints ($x \ge 0$)", "An optimal strategy for managing inventory returns", "A highly efficient scheduling pattern"], "correct": 0},
    {"unit": "Unit 1: Aggregate Planning", "question": "Which of the following is true regarding multi-period aggregate planning horizons?", "options": ["Decisions made in the current period impact capacity, inventory, and choices available in subsequent periods", "Each period is completely independent and has no connection to previous inventory levels", "They can only be solved using greedy priority rules like Shortest Processing Time"], "correct": 0},
    {"unit": "Unit 1: Aggregate Planning", "question": "What does 'backordering' mean within an aggregate planning framework?", "options": ["Purchasing raw components before a demand forecast is generated", "Delaying demand fulfillment to a future period, often incurring a financial penalty cost", "Selling excess capacity to external subcontracting firms"], "correct": 1},
    {"unit": "Unit 1: Aggregate Planning", "question": "How are hiring and firing actions modeled in an APP mathematical programming formulation?", "options": ["As changes in workforce level between period $t-1$ and period $t$", "As fixed parameters that cannot vary across the planning horizon", "By multiplying total demand by the component lead times"], "correct": 0},

    # Unit 2 Multipliers
    {"unit": "Unit 2: Materials Requirement Planning", "question": "What represents a 'Scheduled Receipt' in an MRP time-phased record sheet?", "options": ["An open order that has already been released and is committed to arrive at the start of a specific period", "The quantity of items to be produced in a future planning horizon", "A raw demand forecast pulled from an aggregate planning system"], "correct": 0},
    {"unit": "Unit 2: Materials Requirement Planning", "question": "What is 'Gross Requirements' for a component item in an MRP explosion step?", "options": ["The total un-factored demand generated directly by the planned order releases of its parent items", "The remaining stock available after subtracting safety cushions", "The total financial cost to place a manufacturing order"], "correct": 0},
    {"unit": "Unit 2: Materials Requirement Planning", "question": "In the Silver-Meal Method (SMM), what is the criterion for stopping the grouping of additional periods into a single lot?",
     "options": ["When the average cost per period increases ($AC_{j+1} > AC_j$)", "When total holding costs match ordering costs exactly", "When the workstation line efficiency drops below 80%"], "correct": 0},
    {"unit": "Unit 2: Materials Requirement Planning", "question": "What is a major risk of frequently altering an MRP schedule (system nervousness)?", "options": ["It creates major variations and disruptions in lower-level component requirements and purchasing schedules", "It forces the Bill of Materials to dynamically change its structural graph relationships", "It changes the mathematical objective from cost minimization to profit maximization"], "correct": 0},

    # Unit 3 Multipliers
    {"unit": "Unit 3: Economic Lot Scheduling", "question": "What does 'feasibility' mean in the context of the ELSP?", "options": ["Finding a cyclical schedule that satisfies the demand for all products without any stockouts or overlapping production runs on the shared asset", "Ensuring that the total number of items matches the parent BOM quantities", "Verifying that the line efficiency matches the cycle time exactly"], "correct": 0},
    {"unit": "Unit 3: Economic Lot Scheduling", "question": "What basic genetic algorithm operator mimics biological reproduction by exchanging segments between two chromosomes?", "options": ["Crossover", "Mutation", "Selection Selection"], "correct": 0},
    {"unit": "Unit 3: Economic Lot Scheduling", "question": "What basic genetic algorithm operator introduces random changes to genes to maintain population diversity and avoid local optima?", "options": ["Mutation", "Elitism", "Fitness scaling"], "correct": 0},
    {"unit": "Unit 3: Economic Lot Scheduling", "question": "Why is it valuable to visualize minimum, average, and maximum fitness profiles across generations?", "options": ["To analyze population convergence behavior and determine an effective stopping rule for the GA", "To calculate the exact processing times of individual operations", "To verify if the constraint matrix satisfies total unimodularity"], "correct": 0},

    # Unit 4 Multipliers
    {"unit": "Unit 4: Flow Shop Scheduling", "question": "What parameter is minimized when optimizing Makespan ($C_{max}$)?", "options": ["The absolute completion time of the very last job in the sequence on the final machine", "The total holding cost of items across all warehouse locations", "The total idle time recorded by the first machine in the line"], "correct": 0},
    {"unit": "Unit 4: Flow Shop Scheduling", "question": "In a 2-machine Johnson's algorithm setup, if the shortest processing time occurs on Machine 1, where do you place that job?", "options": ["As early as possible in the job sequence (at the beginning)", "As late as possible in the job sequence (at the end)", "In the middle position of the sequence layout"], "correct": 0},
    {"unit": "Unit 4: Flow Shop Scheduling", "question": "In a 2-machine Johnson's algorithm setup, if the shortest processing time occurs on Machine 2, where do you place that job?", "options": ["As early as possible in the sequence", "As late as possible in the sequence (at the end)", "The job is skipped and not scheduled"], "correct": 1},
    {"unit": "Unit 4: Flow Shop Scheduling", "question": "What is the primary function of calculating lower bounds in Lomnicki's Branch & Bound algorithm?", "options": ["To estimate the best possible makespan for a partial sequence, allowing branches that cannot beat the current best solution to be pruned", "To calculate the average lot size for an MRP explosion step", "To adjust workforce levels dynamically between periods"], "correct": 0},

    # Unit 5 Multipliers
    {"unit": "Unit 5: Job Shop Scheduling", "question": "What does the 'Earliest Due Date' (EDD) priority dispatching rule prioritize?", "options": ["The job with the shortest processing time on the current machine", "The job with the closest, most immediate delivery deadline", "The job that unlocks the largest number of downstream successors"], "correct": 1},
    {"unit": "Unit 5: Job Shop Scheduling", "question": "What happens when a Tabu Search algorithm encounters a solution that satisfies an 'aspiration criterion'?", "options": ["The solution is accepted even if it is currently on the tabu list, often because it beats the best solution found so far", "The algorithm stops immediately and outputs an error log", "The tabu list is cleared completely"], "correct": 0},
    {"unit": "Unit 5: Job Shop Scheduling", "question": "Which scheduling problem is generally considered more complex to solve exactly: an M-machine Permutation Flow Shop or an M-machine Job Shop with diverse routings?", "options": ["The Job Shop problem, due to the customized, independent routing combinations available for each job", "The Permutation Flow Shop, because all jobs must follow the exact same machine sequence", "They possess identical computational structures and matching search space dimensions"], "correct": 0},
    {"unit": "Unit 5: Job Shop Scheduling", "question": "What is the role of a 'converter' when working with Taillard instances for a Job Shop scheduling project?", "options": ["To parse and translate the instance text file into matrices of machine order sequences and operation processing times for your code", "To convert continuous variables into binary integers automatically", "To calculate the total line efficiency score"], "correct": 0},

    # Unit 6 Multipliers
    {"unit": "Unit 6: Job-Resource Assignment", "question": "If an ordinary assignment problem has 5 jobs and 5 resources, how many total feasible assignment combinations exist?", "options": ["$5! = 120$ combinations", "25 combinations", "10 combinations"], "correct": 0},
    {"unit": "Unit 6: Job-Resource Assignment", "question": "What is a defining characteristics of binary decision variables in an optimization model?", "options": ["They can take any fractional value between 0.0 and 1.0", "They are strictly constrained to take a value of either exactly 0 or exactly 1", "They are used to represent continuous processing times"], "correct": 1},
    {"unit": "Unit 6: Job-Resource Assignment", "question": "In an ordinary assignment model constraint $\sum_{j} x_{ij} = 1$, what does this mathematically ensure for each job $i$?", "options": ["That job $i$ is assigned to exactly one resource", "That resource $j$ can accept up to 5 individual tasks", "That the total cost of assignment remains equal to 1"], "correct": 0},
    {"unit": "Unit 6: Job-Resource Assignment", "question": "What property of the Hungarian Method makes it highly efficient for solving ordinary assignment problems?", "options": ["It solves the problem in polynomial time ($O(n^3)$) rather than searching through all $n!$ combinations", "It uses random mutation strings to explore a population of assignment patterns", "It eliminates the need for an input cost matrix structure"], "correct": 0},

    # Unit 7 Multipliers
    {"unit": "Unit 7: Mixed Model Sequencing", "question": "What type of assembly line configuration is the primary target for Mixed-Model Sequencing models?", "options": ["A single flexible line where different models or variants of a product are assembled simultaneously without requiring long shutdown setups", "A traditional batch line that shuts down for days to swap tooling infrastructure between variants", "A line dedicated exclusively to a single uniform standard product model"], "correct": 0},
    {"unit": "Unit 7: Mixed Model Sequencing", "question": "What core issue is minimized when smoothing component consumption under Monden's Method?", "options": ["The risk of line overloads or stock depletions caused by a variable and highly erratic component demand pattern", "The total financial cost of placing orders with raw component suppliers", "The number of active workstations utilized across the factory layout"], "correct": 0},
    {"unit": "Unit 7: Mixed Model Sequencing", "question": "In a Genetic Algorithm for MMSP, what problem can arise if an invalid chromosome sequence is generated during crossover?", "options": ["The sequence might violate production quantities, requiring specialized repair heuristics or penalty functions to maintain validity", "The Pyomo modeling language will crash and corrupt the dataset files", "The problem automatically turns into a 2-machine flow shop model"], "correct": 0},
    {"unit": "Unit 7: Mixed Model Sequencing", "question": "What does 'Option B' for chromosome encoding typically involve in mixed-model sequencing optimization models?", "options": ["Encoding genes as sequence positions rather than direct product identity codes", "Eliminating the genetic algorithm population entirely to prioritize constructive rules", "Representing monthly hiring levels as integer numbers"], "correct": 0},

    # Unit 8 Multipliers
    {"unit": "Unit 8: Assembly Line Balancing", "question": "What is 'Line Balancing Delay' within an ALBP context?", "options": ["The total percentage of idle time across the assembly line ($1 - \eta$)", "The lead time delay associated with procuring components from external suppliers", "The time required to reset a machine's configuration for a different product variant"], "correct": 0},
    {"unit": "Unit 8: Assembly Line Balancing", "question": "What does a 'workstation time' ($T_s$) represent in line balancing metrics?", "options": ["The sum of the processing times of all individual tasks assigned to that specific workstation $s$", "The time an operator takes to walk from one department to another", "The total time allowed to complete all jobs across all active machines"], "correct": 0},
    {"unit": "Unit 8: Assembly Line Balancing", "question": "What type of variable is typically used in a mathematical optimization formulation to represent whether a task $i$ is assigned to a workstation $s$?", "options": ["A binary decision variable ($x_{is} \in \{0, 1\}$)", "A continuous variable mapping capacity usage rates", "An integer variable representing workforce hiring levels"], "correct": 0},
    {"unit": "Unit 8: Assembly Line Balancing", "question": "What is the primary benchmark goal of the Type 1 Assembly Line Balancing Problem (ALBP-1)?", "options": ["Minimizing the number of workstations required for a fixed, predetermined cycle time", "Minimizing the cycle time for a fixed, predetermined number of workstations", "Maximizing the sequence-dependent setup costs across a shared machine asset"], "correct": 0},

    # Unit 9 Multipliers
    {"unit": "Unit 9: Resource Allocation", "question": "What is a core constraint often modeled in a Manpower Scheduling Method (MSM) framework?", "options": ["Ensuring staff availability matches task workloads while respecting constraints like max working hours, shift structures, or skill requirements", "Ensuring that all tasks follow a uniform, single routing path across all machines", "Forcing the inventory levels to balance with time-phased component requirements"], "correct": 0},
    {"unit": "Unit 9: Resource Allocation", "question": "What parameter does an optimization model minimize if its objective is focused on workforce balancing?", "options": ["The total costs associated with resource deployment, under-utilization, over-time, or skill mismatches", "The number of downstream successors linked within a line precedence graph", "The total makespan of jobs moving through a sequence of machines"], "correct": 0},
    {"unit": "Unit 9: Resource Allocation", "question": "What value does an automated synthetic data generator provide when testing optimization code?", "options": ["It allows you to systematically test the algorithm's scalability and robustness by generating problems of varying sizes", "It proves mathematically that a heuristic solution matches the absolute global optimum", "It eliminates the need to compile constraints or objective functions in Pyomo"], "correct": 0},
    {"unit": "Unit 9: Resource Allocation", "question": "What template name and archive format should be used to submit your homework assignments for this course?", "options": ["The MUCEIM_PO_2026 template in a ZIP file named with your surname and name", "An uncompressed text file containing your raw Python output log script", "A PDF report uploaded directly without its associated Python source files"], "correct": 0},

    # Fillers to achieve exact 115 item target depth across materials
    {"unit": "Unit 1: Aggregate Planning", "question": "What does a 'Mixed Strategy' in Aggregate Production Planning combine?", "options": ["Elements of both chase and level strategies, adjusting workforce and inventory levels concurrently to optimize costs", "Continuous linear variables with non-linear exponential setup parameters", "BOM explosion charts with local Tabu search lists"], "correct": 0},
    {"unit": "Unit 2: Materials Requirement Planning", "question": "What does 'Netting' mean in the context of the MRP explosion logic steps?", "options": ["Subtracting current on-hand inventory and scheduled receipts from gross requirements to find the true needed quantities", "Multiplying order costs by holding costs to determine lot sizes", "Sorting tasks by the number of downstream followers in a precedence graph"], "correct": 0},
    {"unit": "Unit 3: Economic Lot Scheduling", "question": "What challenge occurs in ELSP when the total required production time for all items exceeds available capacity?", "options": ["The problem becomes mathematically infeasible, as demand cannot be satisfied regardless of the sequence", "The algorithm automatically switches to a Type 1 line balancing model", "The unit holding costs are reduced to zero to restore balance"], "correct": 0},
    {"unit": "Unit 4: Flow Shop Scheduling", "question": "What type of diagram visually displays the schedule of jobs across different machines over time?", "options": ["Gantt Chart", "Precedence Graph Diagram", "Bill of Materials Hierarchy Tree"], "correct": 0},
    {"unit": "Unit 5: Job Shop Scheduling", "question": "What does the 'Shortest Processing Time' (SPT) rule tend to minimize when used as a dispatching heuristic?", "options": ["Average job lateness and mean flow time across the shop floor", "The sequence-dependent configuration setup costs", "The number of workstations required for a fixed cycle time"], "correct": 0},
    {"unit": "Unit 6: Job-Resource Assignment", "question": "What does a cost matrix entry of infinity ($\infty$) signify in an assignment problem?", "options": ["An impossible or forbidden assignment link that the optimization model cannot choose", "A zero-cost dummy shortcut that balances the matrix dimensions", "An assignment that maximizes line balancing efficiency scores"], "correct": 0},
    {"unit": "Unit 7: Mixed Model Sequencing", "question": "What occurs during a 'mutation' step in an MMSP Genetic Algorithm run?", "options": ["Two random genes within a chromosome sequence are swapped to maintain exploration diversity", "The entire population is replaced by copies of the best individual solution", "A linear relaxation step is executed to remove integer bounds"], "correct": 0},
    {"unit": "Unit 8: Assembly Line Balancing", "question": "What is the primary goal of the Type 2 Assembly Line Balancing Problem (ALBP-2)?", "options": ["Minimizing the cycle time for a fixed, predetermined number of workstations", "Minimizing the number of workstations for a fixed cycle time", "Maximizing the total sum of assignment costs across a square matrix"], "correct": 0},
    {"unit": "Unit 9: Resource Allocation", "question": "What is an operational benefit of establishing a lower optimization GAP percentage in an MILP solver?", "options": ["It forces the solver to continue searching until it finds a solution closer to the absolute mathematical optimum", "It converts all integer parameters into continuous variables to accelerate execution", "It automatically generates a synthetic dataset for testing purposes"], "correct": 0},
    {"unit": "Unit 1: Aggregate Planning", "question": "In Pyomo, what object structural type is utilized to define the optimization goals like minimizing cost?", "options": ["Objective", "Constraint", "Var"], "correct": 0},
    {"unit": "Unit 2: Materials Requirement Planning", "question": "What does 'Lotification' mean within an inventory planning framework?", "options": ["The process of grouping time-phased net requirements into discrete production or purchasing batches", "The mapping of assembly line operations across a set of workstations", "The calculation of lower bounds in a Branch & Bound algorithm step"], "correct": 0},
    {"unit": "Unit 3: Economic Lot Scheduling", "question": "What does 'population size' represent inside a Genetic Algorithm metaheuristic setup?", "options": ["The number of candidate solution chromosomes maintained simultaneously in each generation loop", "The total number of manufacturing operators available on the plant floor", "The quantity of product units to be produced in a single batch"], "correct": 0},
    {"unit": "Unit 4: Flow Shop Scheduling", "question": "What assumption is made about job processing in a standard deterministic Flow Shop scheduling model?", "options": ["Processing times are known constants and operations cannot be interrupted", "Processing times are random variables that change during execution", "Jobs can move backward to previous machines in the layout"], "correct": 0},
    {"unit": "Unit 5: Job Shop Scheduling", "question": "What is a 'neighborhood move' in local search metaheuristics like Tabu Search?",
     "options": ["An operational change applied to a current solution sequence to generate its adjacent candidate solutions", "The relocation of an assembly workstation to a different factory department", "The addition of a new component level to a product's BOM tree"], "correct": 0},
    {"unit": "Unit 6: Job-Resource Assignment", "question": "What does 'totally unimodular' mean regarding a constraint matrix?", "options": ["Its linear relaxation extreme points are guaranteed to be integer, allowing linear programming solvers to find exact integer optimums", "It can only be processed using heuristic priority rules like LCR", "It contains an infinite number of alternative optimal solutions"], "correct": 0},
    {"unit": "Unit 7: Mixed Model Sequencing", "question": "What is an 'infeasible sequence' within an MMSP execution context?", "options": ["A candidate sequence that fails to produce the exact product quantities required by the demand target", "A schedule that utilizes more than two machines simultaneously", "A sequence that groups products of identical colors together"], "correct": 0},
    {"unit": "Unit 8: Assembly Line Balancing", "question": "What parameter is typically plotted on a precedence graph for an assembly line balancing instance?", "options": ["Nodes representing individual manufacturing tasks and directed links showing their sequential technological dependencies", "Monthly demand curves alongside aggregate workforce hiring profiles", "The fitness value progression across successive generation loops"], "correct": 0},
    {"unit": "Unit 9: Resource Allocation", "question": "What does 'under-utilization' of a resource typically incur in an operational allocation context?", "options": ["An efficiency penalty or financial loss, as capacity is paid for but not leveraged productively", "An automatic reduction in the technological precedence requirements of a line", "A transition from a generalized assignment problem to an ordinary assignment problem"], "correct": 0}
]

def get_randomized_exam(num_questions=100):
    """
    Shuffles the master question database and returns a fresh slice 
    of the requested size. This ensures every simulation run is unique.
    """
    pool = list(RAW_QUESTION_BANK)
    random.shuffle(pool)
    selected_questions = pool[:min(num_questions, len(pool))]
    return selected_questions

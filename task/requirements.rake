desc 'Verifies the requirements'
task :requirements do
  require 'cliver'

  Cliver.detect!('python2.6', '~> 2.6')
  Cliver.detect!('pip', '>= 1.3')
end

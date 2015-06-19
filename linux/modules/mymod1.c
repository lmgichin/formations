#include <linux/module.h>
#include <linux/init.h>

MODULE_AUTHOR("gichin");
MODULE_DESCRIPTION("exemple de module");
MODULE_SUPPORTED_DEVICE("none");
MODULE_LICENSE("none");

static int param;

module_param(param, int, 0);
MODULE_PARM_DESC(param, "Un paramètre de ce module");

static int __init mymod_init(void)
{

	printk(KERN_DEBUG "Message de mon module\n");
	printk(KERN_DEBUG "param = %d\n", param);
	return 0;
}

static void __exit mymod_exit(void)
{
	printk(KERN_DEBUG "Ciao...\n");
}


module_init(mymod_init);
module_exit(mymod_exit);
